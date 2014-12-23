# -*- coding: utf-8 -*-

# Import python libs
import sys

# Import salt libs
from salt.exceptions import CommandExecutionError
from salt.modules.aptpkg import _strip_uri
from salt.state import STATE_INTERNAL_KEYWORDS as _STATE_INTERNAL_KEYWORDS


def __virtual__():
    '''
    Only load if modifying repos is available for this package type
    '''
    return 'pkg.mod_repo' in __salt__


def _error(ret, err_msg):
    ret['result'] = False
    ret['comment'] = err_msg
    return ret


