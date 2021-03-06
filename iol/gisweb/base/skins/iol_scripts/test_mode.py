## Script (Python) "test_mode"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=default=False,json=False
##title=Is app in test mode?
##
"""
Returns True or False

Ti dice se la applicazione di cui fa parte il documento o il form è in test.
La funzione interroga la proprietà del plominodb <iol_tipo_app>_is_in_test.
Se la variabile non è settata restituisce il valore di default.
"""

attr_list = ['app_in_test']

try:
    iol_tipo_app = context.naming('iol_tipo_app')
except Exception as err:
   iol_tipo_app = ''

if iol_tipo_app:
    attr_list.append('%s_is_in_test' % iol_tipo_app)

db = context.getParentDatabase()

for attr_name in attr_list:
    try:
        test = getattr(db, attr_name)
    except:
        pass
    else:
        default = test
        
if json:
    from Products.CMFPlomino.PlominoUtils import json_dumps
    return json_dumps(default)
else:
    return default
