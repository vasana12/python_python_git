#-*-coding:utf8 -*-

list1=[]
list2=[]

while(True):
    i=0;
    j=0;
    a=input("학번 입력 =>")
    if(a!='exit'):
        list1.append(a)
        print(list)
    elif(a=='exit'):
        break
    list[i][j]=input("이름 입력=>")
    j += 1
    list[i][j]=int(input("국어점수 입력=>"))
    j += 1
    list[i][j]=int(input("영어점수 입력=>"))
    j += 1
    list[i][j]=int(input("수학점수 입력=>"))
    j += 1
    list[i][j]=dict.get('kor')+dict.get('eng')+dict.get('math')
    j += 1
    list[i][j]=dict.get('total')/3
    j += 1
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
    i+=i

s= "성적표"
print(s.center(47,"*"))
print("="*50)
print("학번     이름   국어   영어   수학   총점   평균   등급")
print("="*50)
i=0;
j=0;
for i in list[i]:
    print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
        (list[i][j],list[i][j+1],list[i][j+2],list[i][j+3],
         list[i][j+4],list[i][j+5],list[i][j+6],list[i][j+7]))