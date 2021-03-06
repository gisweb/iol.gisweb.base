## Script (Python) "isConditionVerified"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=obj=None, cond=''
##title=Script che renderizza i dati base della pratica



from Products.CMFPlomino.PlominoUtils import json_loads, json_dumps, DateToString, Now, open_url


if not obj:
    return False
if obj.portal_type=='PlominoDatabase':
    result=dict(
        cantieri=dict(
            rinnovo=True,
            proroga=True,
            integrazione=True
        )
    )
    try:
        res=result[application][cond]
    except:
        res=False
elif obj.portal_type=='PlominoDocument':
    #Applicazione Trasporti Eccezionali
    # A) Condizioni di Integrabilità :
    #    1) Pratica in corso di Validità 
    # B) Condizioni di prorogabilità :
    #    1) Pratica in corso di Validità
    #    2) Massimo 1 Proroga
    #    3) Tipo Richiesta singola o multipla
    # C) Condizioni di Rinnovo
    #    1) Pratica a un mese dalla scadenza o scaduta da un mese
    #    2) Tipo Richiesta periodica
    today = Now()
    start = obj.getItem('autorizzata_dal')
    end = obj.getItem('autorizzata_al')
    tipoRichiesta = obj.getItem('iol_tipo_richiesta')
    dovuto = context.getItem('dovuto',0)
    pagato = context.getItem('pagato',0)
    debito = 0
    if dovuto and pagato:
        debito = dovuto - pagato

    if cond=='rinnovo' and debito <= 0:
        if obj.getItem('durata_occupazione') == 'permanente':
        #if ((today > start) and ((end + 30) > today)  and ((end - 30) < today)):
        #nrinnovi=obj.getItem('numero_rinnovi')
        #if ((today > start) and ((end + 30) > today)  and ((end - 30) < today)) and obj.getItem('rinnovabile',0)==1 and nrinnovi<4:
            res = True
        else:
            res = False   
    
    else:
        res = False
else:
    res = False
return res
