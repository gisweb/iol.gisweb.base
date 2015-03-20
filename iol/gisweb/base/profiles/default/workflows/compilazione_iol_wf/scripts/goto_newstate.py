## Script (Python) "goto_newstate"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=state_change
##title=
##
from Products.CMFPlomino.PlominoUtils import StringToDate, json_loads
doc = state_change.object
frm = doc.wf_getInfoFor("wf_formname")
app = doc.getItem("iol_tipo_app","default")
doc.setItem("Form","frm_%s_%s" %(app,frm))

#if not doc.wf_getInfoFor('wf_presentata') and not doc.getItem('documenti_autorizzazione') and frm=='completata':  
#    doc.setItem('Form','frm_%s_stampa' %(app))
#    info = json_loads(doc.printModelli(doc.getParentDatabase().getId()))
    
#    model = info['modello_scia_savona.docx']['model']
#    field = info['modello_scia_savona.docx']['field']
    
#    grp = 'autorizzazione'
    
#    context.createDoc(model=model,field=field,grp=grp)
#    context.setItem('Form','frm_%s_completata' %(app))
  #  context.convertToPdf(file_type='documenti_autorizzazione')
