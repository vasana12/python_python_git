#-*-coding:utf8 -*-
dict={}

dict['hakbun']=input("학번 입력 =>")
dict['irum']=input("이름 입력=>")
dict['kor']=int(input("국어점수 입력=>"))
dict['eng']=int(input("영어점수 입력=>"))
dict['math']=int(input("수학점수 입력=>"))
dict['total']=dict.get('kor')+dict.get('eng')+dict.get('math')
dict['avg']=dict.get('total')/3

if dict.get('avg') >=90:
    dict['grade']="수"
elif dict.get('avg') >=80:
    dict['grade'] = "우"
elif dict.get('avg') >=70:
    dict['grade'] = "미"
elif dict.get('avg') >=60:
    dict['grade'] = "양"
else:
    dict['grade'] = "가"
s= "성적표"
print(s.center(47,"*"))
print("="*50)
print("학번     이름   국어   영어   수학   총점   평균   등급")
print("="*50)
print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
      (dict['hakbun'],dict['hakbun'],dict['kor'],dict['eng'],
       dict['math'],dict['total'],dict['avg'],dict['grade']))