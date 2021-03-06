## Script (Python) "isConditionVerified"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= doc='', wf_id='iol_workflow'
##title=Script che renderizza i dati base della pratica
##
#                                                                                              #
#                                                                                              #
#                                                                                              #
#                                                                                              #
#                                                                                              #
#                                                                                              #
#                                                                                              # 
################################################################################################

#if not context.portal_type in ('PlominoForm','PlominoDocument'):
 #   return '<div class="error">Il contesto non è ne un documento se un form. %s</div>' %(context.portal_type)

#Plomino Database    

from Products.CMFCore.utils import getToolByName

db = doc.getParentDatabase()



#Risultato
html=''
#oggetto REQUEST
request = context.REQUEST

#Recupero informazioni sullo stato di workflow e del documento
if doc.portal_type=='PlominoForm':
    frmName = doc.getFormName()
    doc=None
    state = None
    actions = []
    wfVars = dict()
    editMode = True
    creationMode = True

elif doc.portal_type=='PlominoDocument':
    
    #return '<div class="error">%s</div>' %(doc.getForm().getFormName())
    frmName = doc.getForm().getFormName()
    info = doc.docInfo(format='')
    state = info['review_state'][0]['id']
    actions = info['review_state'][0]['transitions']
    wfVars = info['wf_vars'][wf_id]
    editMode = doc.isEditMode()
    creationMode = False

if doc and state == 'avvio':
    frm = db.getForm('base_sub_invio_domanda')
    html += frm.displayDocument(doc,editmode=editMode,parent_form_id=frmName)


if doc:
    frm = db.getForm('base_sub_numerazione')
    html += frm.displayDocument(doc,editmode=editMode,parent_form_id=frmName)

if doc and state=='autorizzata':
    frm = db.getForm('base_sub_autorizzazione')
    html += frm.displayDocument(doc,editmode=editMode,parent_form_id=frmName)

if doc:
    frm = db.getForm('base_sub_workflow')
    html += frm.displayDocument(doc,editmode=editMode,parent_form_id=frmName)




return html    