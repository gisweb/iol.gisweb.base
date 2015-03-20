## Script (Python) "before_h1"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=state_change
##title=
##
from DateTime import DateTime
from Products.CMFPlomino.PlominoUtils import StringToDate, json_loads
doc = state_change.object

doc.setItem('data_presentazione',DateTime().strftime('%d/%m/%Y'))



info = json_loads(doc.printModelli(doc.getParentDatabase().getId(),grp='distinta',field='documenti_distinta'))
model = info['modello_distinta_savona.docx']['model']
field = info['modello_distinta_savona.docx']['field']

grp = 'autorizzazione'

doc.createDoc(model=model,field=field,grp=grp)
