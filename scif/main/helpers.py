'''

Copyright (C) 2017 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2017 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from scif.utils import run_command as run_cmd
from scif.logger import bot
import shlex
import sys
import os
import re

def get_parts(pair, default=None):
    '''pair is expected to be a string with some key, value, and this function
       will replace any "=" with a space, and then parse the remainder
       for a first and second part (key and value pair). 

       We likely will need to use regular expressions for pairs that have 
       spaces or equals that need to be maintained.

       Parameters
       ==========
       pair should be a single string, likely with a key and value split by 
            a space or equals sign.
    '''
    pair = pair.replace('=',' ')
    parts = pair.split(' ')
    src = parts[0].strip()
    if len(parts) == 1:
        dest = default
    else:
        dest = parts[1].strip()
    return src,dest


def run_command(self, cmd, spinner=True):
    '''run_install will run a command (a list) and wrap in a spinner. A 
       result (dict) with message and return code is returned. If the
       return value is not 0, an error is issed and we exit
    '''
    if spinner is True:
        bot.spinner.start()
    
    result = run_cmd(cmd)

    if spinner is True:
        bot.spinner.stop()
    retval = result['return_code']
    if retval != 0:
        bot.error('Return code %s' %retval)
        sys.exit(retval)
    return result



def parse_entrypoint(entry_point=None):
    '''parse entrypoint will return a list, where the first argument is the
       executable, followed by arguments
 
       Parameters
       ==========
       entry_point: the entry point for the application, is 
    '''

    if entry_point is None:
        from scif.defaults import SCIF_ENTRYPOINT as entry_point

    # We expect an [executable, arg1, arg2]
    if not isinstance(entry_point, list):
        entry_point = [entry_point]

    # Any [e] in the command or entrypoint (command line) are environment vars
    entry_point= ' '.join(entry_point)
    entry_point = re.sub('\[e\]','$', entry_point)

    # Split into executable, arguments
    return shlex.split(entry_point)
