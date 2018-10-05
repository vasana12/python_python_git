kor=int(input("국어 점수를 입력하세요=>"))
eng=int(input("영어 점수를 입력하세요=>"))
mat=int(input("수학 점수를 입력하세요=>"))
tot=kor+eng+mat
avg=tot/3.0
print("tot={:5d}".format(tot))
print("avg={:6.2f}".format(avg)) #평균을 출력하는 format서식을 지정한다.