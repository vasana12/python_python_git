#-*-coding:utf8 -*-
list_rec=[]

list_rec.append(input("학번 입력 =>"))
list_rec.append(input("이름 입력 =>"))
list_rec.append(int(input("국어점수 입력=>")))
list_rec.append(int(input("영어점수 입력=>")))
list_rec.append(int(input("수학점수 입력=>")))

list_rec.append(list_rec[2] + list_rec[3] + list_rec[4])
list_rec.append(list_rec[5]/3)
if list_rec[6] >=90:
    list_rec.append("수")
elif list_rec[6] >=80:
    list_rec.append("우")
elif list_rec[6] >=70:
    list_rec.append("미")
elif list_rec[6] >=60:
    list_rec.append("양")
else:
    list_rec.append("가")
s= "성적표"
print(s.center(47,"*"))
print("="*50)
print("학번     이름   국어   영어   수학   총점   평균   등급")
print("="*50)
print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
      (list_rec[0],list_rec[1],list_rec[2],list_rec[3],
       list_rec[4],list_rec[5],list_rec[6],list_rec[7]))