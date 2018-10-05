#-*-coding:utf8 -*-
my_dic={'id':'Dominica','pw':'a12341','db':'Oracle'}
print(my_dic)
print(my_dic['id']) #키로 값을 추출
my_dic['id']="PYTHON"
print(my_dic)
print(my_dic['pw']) #키로 값을 추출
print(my_dic['db']) #키로 값을 추출

del my_dic['id']
print(my_dic)

my_dic['irum']='이기자' #값 변경
print(my_dic)
print(my_dic.get('irum'))

