import json

s=u'''{"name":"RuRi",
"brothers":["RuSe","RuO"],
"addr":"Toronto"}'''

class JsonObject:
    def __init__(self,d):
        self.__dict__ = d       #dict 형태로 변환시켜줌
if __name__ == '__main__':
    data = json.loads(s, object_hook=JsonObject)
    print(data.name)
    print(data.addr)
    for brother in data.brothers:
        print(brother)