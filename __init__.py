#!/usr/bin/env python3

# Copyright (C) 2016 - 2018 Sylvia van Os <sylvia@hackerchick.me>
#
# Pext emoji module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import string

from xml.etree.ElementTree import parse

from pext_base import ModuleBase
from pext_helpers import Action


class Module(ModuleBase):
    def init(self, settings, q):
        self.settings = settings
        self.q = q

        self.entries = {}
        self.display_entries = []

        self._get_entries()

    def _get_entries(self):
        self.emoji_translations = {}

        translation_files = ['annotations-{}.xml'.format(self.settings['_locale']),
                             'annotationsDerived-{}.xml'.format(self.settings['_locale'])]

        for translation_file in translation_files:
            try:
                emoji_translation_xml = parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), translation_file)).getroot()[1]
                for annotation in emoji_translation_xml:
                    if 'type' in annotation.attrib and annotation.attrib['type'] == 'tts':
                        self.emoji_translations[annotation.attrib['cp']] = annotation.text
            except Exception:
                pass

        current_group = ""
        current_subgroup = ""
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'emoji-test.txt'), 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                if line.startswith('# group: '):
                    current_group = string.capwords(line[len('# group :'):].strip())
                    current_subgroup = ""
                elif line.startswith('# subgroup: '):
                    current_subgroup = string.capwords(line[len('# subgroup :'):].replace('-', ' ').strip())
                elif not line.startswith('#'):
                    try:
                        if line.split('#')[0].split(';')[1].strip() == 'non-fully-qualified':
                            continue

                        emoji, code = line.split('#', 1)[1].strip().split(' ', 1)
                        try:
                            code = self.emoji_translations[emoji]
                        except KeyError:
                            pass
                    except IndexError:
                        continue

                    identifier = '{} {} ({} - {})'.format(emoji, string.capwords(code.strip()), current_group, current_subgroup)
                    self.entries[identifier] = emoji

        self.display_entries = sorted(list(self.entries.keys()))
        self.q.put([Action.replace_entry_list, self.display_entries])

    def stop(self):
        pass

    def selection_made(self, selection):
        if len(selection) == 0:
            self.q.put([Action.replace_entry_list, self.display_entries])
        elif len(selection) == 1:
            self.q.put([Action.copy_to_clipboard, self.entries[selection[0]["value"]]])
            self.q.put([Action.close])

    def process_response(self, response):
        pass
