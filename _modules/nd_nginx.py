# -*- coding: utf-8 -*-

# TODO: We should add the capability to do u+r type operations here
# some time in the future

from __future__ import print_function

# Import python libs
import contextlib  # For < 2.7 compat
import datetime
import difflib
import errno
import fileinput
import fnmatch
import itertools
import logging
import operator
import os
import re
import shutil
import stat
import sys
import tempfile
import time
import glob

try:
    import grp
    import pwd
except ImportError:
    pass

# Import salt libs
import salt.utils
import salt.utils.find
import salt.utils.filebuffer
import salt.utils.files
import salt.utils.atomicfile
from salt.exceptions import CommandExecutionError, SaltInvocationError
import salt._compat

log = logging.getLogger(__name__)


def __virtual__():
    '''
    Only work on POSIX-like systems
    '''
    # win_file takes care of windows
    if salt.utils.is_windows():
        return False
    return True

def _error(ret, err_msg):
    '''
    Common function for setting error information for return dicts
    '''
    ret['result'] = False
    ret['comment'] = err_msg
    return ret

def test():
    ret ={}
    try:
        f=open('log.txt','a')
        f.write()
    except Exception,e:
        ret['result'] = False
        ret['comment'] = e
        return ret


