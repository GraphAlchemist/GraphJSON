import json
import urllib2


file = open("bacon.json", "w")
data = urllib2.urlopen("http://movies.graphalchemist.com/movies-graph/13810/61016/").read()
GraphJSON = json.loads(data)


GraphJSON['edges'] = GraphJSON.pop('links')

for n in GraphJSON['nodes']:
    if n.get('id'):
        n['_id'] = n.pop('id')
    data = {}
    style = {}
    for k, v in list(n.iteritems()):    
        #import pdb; pdb.set_trace()
        if (k == "_id") or (k =="data") or (k=="style"):
            continue
        elif k == "label":
            style['caption'] = n.pop(k)
        else:
            data[k] = n.pop(k)
    if (style == {}) or (data=={}):
        continue
    n['style'] = style
    n['data'] = data

for e in GraphJSON['edges']:
    if e.get('source'):
        e['_source'] = e.pop('source')
    if e.get('target'):
        e['_target'] = e.pop('target')
    data = {}
    style = {}
    for k, v in list(e.iteritems()):    
        #import pdb; pdb.set_trace()
        if (k == "_source") or (k =="_target") or (k=="style") or (k=="data"):
            continue
        elif k == "label":
            style['caption'] = e.pop(k)
        else:
            data[k] = e.pop(k)
    if (style == {}) or (data=={}):
        continue
    e['style'] = style
    e['data'] = data

json.dump(GraphJSON, file, sort_keys=True, indent=4, separators=(',', ': '))