import json

data= [{'a':'A','b':(1,2), 'c':9.75}]
data_string = json.dumps(data)  #파이썬형태의 데이터를 문자열로 변환시키기
print('ENCODED:', data_string)

decoded = json.loads(data_string)   #문자열을 JSON 으로 변환시켜서 저장
print('DECODE:',decoded)

print('ORIGINAL:', type(data[0]['b']))
print('DECODE:', type(decoded[0]['b']))