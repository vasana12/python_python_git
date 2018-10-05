
def sungjuk_output(lst):
    s= "성적표"
    print(s.center(47,"*"))
    print("="*50)
    print("학번     이름   국어   영어   수학   총점   평균   등급")
    print("="*50)
    for data in lst:
        print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
          (data['hakbun'],data['irum'],data['kor'],data['eng'],
           data['math'],data['total'],data['avg'],data['grade']))
    else:
        print("="*50)