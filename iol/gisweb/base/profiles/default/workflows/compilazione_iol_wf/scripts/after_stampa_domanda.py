## Script (Python) "after_stampa_domanda"
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
    
    
info = json_loads(doc.printModelli(doc.getParentDatabase().getId(),grp='distinta',field='documenti_distinta'))
model = info['modello_distinta_savona.docx']['model']
field = info['modello_distinta_savona.docx']['field']

grp = 'distinta'

doc.createDoc(model=model,field=field,grp=grp,redirect_url=context.absolute_url())
