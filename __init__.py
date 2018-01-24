#!/usr/bin/env python3

# Copyright (C) 2016 - 2017 Sylvia van Os <sylvia@hackerchick.me>
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

from emoji import unicode_codes

from pext_base import ModuleBase
from pext_helpers import Action, Entry, EntryType


class Module(ModuleBase):
    def init(self, settings, q):
        self.q = q

        self.entries = []

        self._get_entries()

    def _get_entries(self):
        for emoji, code in sorted(unicode_codes.UNICODE_EMOJI.items()):
            identifier = '{0} {1}'.format(emoji, code)
            entry = Entry(identifier, copyname=emoji, type=EntryType.copyable)
            self.entries.append(entry)
            self.q.put([Action.add_entry, entry])

    def stop(self):
        pass

    def selection_made(self, selection):
        if len(selection) == 0:
            for entry in self.entries:
                self.q.put([Action.add_entry, entry])

    def process_response(self, response):
        pass
