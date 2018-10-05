import json

data = [{'a':'A','b':(2,4),'c':3.0}]
print(data)
print('DATA:', repr(data))

data_string= json.dumps(data)
print('JSON',data_string)