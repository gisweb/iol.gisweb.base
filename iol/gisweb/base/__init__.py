from AccessControl import allow_module
allow_module('iol.gisweb.base.scripts.frm_beforeCreateDocument')
allow_module('iol.gisweb.base.pgReplication')

import permissions

from permissions import IOL_READ_PERMISSION, IOL_EDIT_PERMISSION, IOL_REMOVE_PERMISSION

from dict2xml import dict2xml
