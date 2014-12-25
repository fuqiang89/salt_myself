# -*- coding: utf-8 -*-

# Import python libs
import sys

# Import salt libs
from salt.exceptions import CommandExecutionError
from salt.modules.aptpkg import _strip_uri
from salt.state import STATE_INTERNAL_KEYWORDS as _STATE_INTERNAL_KEYWORDS
# __virtualname__ = 'nd_nginx'
#
# def __virtual__():
#
#     return __virtualname__



'''
configure arguments:
--prefix=/usr/local/nginx-1.6.2
--with-http_flv_module
--with-http_mp4_module
--with-http_stub_status_module
--with-http_ssl_module
--with-pcre=/usr/local/src/nginx_install/pcre-8.36
--with-zlib=/usr/local/src/nginx_install/zlib-1.2.8
--with-openssl=/usr/local/src/nginx_install/openssl-1.0.1j
--add-module=
'''

def _error(ret, err_msg):
    ret['result'] = False
    ret['comment'] = err_msg
    return ret

def installed(name,
            source=None,
            source_hash='',
            add_module=None,
            configure=None,
            prefix=None,
            **kwargs):
    ret={}
    try:
        __salt__['nd_nginx.test'](source)
    except Exception,e:
        return _error(ret,e)
