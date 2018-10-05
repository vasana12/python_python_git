#-*-coding: utf-8 -*-
import json
jsonData = """
{
    "snapshot":{
        "repos": "test.com/repositories/snapshots",
        "userid": "id",
        "passwd": "1234"
    },
    "release" :{
        "repos" : "test.com/repositories/release",
        "userid" : "id",
        "passwd" : "5678"
    },
    "component":{
        "test":"test.com"
    }
}
"""
data_json = json.loads(jsonData) #json 형식의 문자열을 파이썬의 타입으로 변경(딕셔너리).
print(type(data_json))
print(data_json)
print(data_json['component']['test'])
data_str = json.dumps(data_json) #json 형식의 데이터를 문자열 형태로 변경
#data_str = json.dumps(data_json, indent=4)
print(type(data_str))
print(data_str)