from Products.CMFCore import permissions as CMFCorePermissions
from AccessControl.SecurityInfo import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles

security = ModuleSecurityInfo('iol.gisweb.base')

security.declarePublic('IOL_READ_PERMISSION')
IOL_READ_PERMISSION = 'iol.gisweb.base: Read iol documents'
setDefaultRoles(IOL_READ_PERMISSION, ())

security.declarePublic('IOL_EDIT_PERMISSION')
IOL_EDIT_PERMISSION = 'iol.gisweb.base: Edit iol documents'
setDefaultRoles(IOL_EDIT_PERMISSION, ())

security.declarePublic('IOL_REMOVE_PERMISSION')
IOL_REMOVE_PERMISSION = 'iol.gisweb.base: Delete iol documents'
setDefaultRoles(IOL_REMOVE_PERMISSION, ())
