#!/usr/bin/env python3

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
from pext_helpers import Action


class Module(ModuleBase):
    def init(self, settings, q):
        self.q = q

        self.entries = {}

        self._get_entries()

    def _get_entries(self):
        for emoji, code in sorted(unicode_codes.UNICODE_EMOJI.items()):
            identifier = '{0} {1}'.format(emoji, code)
            self.entries[identifier] = emoji
            self.q.put([Action.add_entry, identifier])

    def stop(self):
        pass

    def selection_made(self, selection):
        if len(selection) == 0:
            self.q.put([Action.replace_entry_list, sorted(list(self.entries.keys()))])
        elif len(selection) == 1:
            self.q.put([Action.copy_to_clipboard, self.entries[selection[0]["value"]]])
            self.q.put([Action.close])

    def process_response(self, response):
        pass
