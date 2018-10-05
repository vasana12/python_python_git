import json

obj_json = u'{"str2": [42.2], "str1":42}'
obj =json.loads(obj_json)
print(repr(obj))
print(obj)
print(json.dumps(obj, indent=4,sort_keys=True))