import sqlite3
dbconn = sqlite3.connect('tel.db')

dbcursor = dbconn.cursor()
class Sungjuk:
    def __init__(self):
        self._hakbun = None
        self._irum = None
        self._kor = 0
        self._eng = 0
        self._math= 0
        self._tot= 0
        self._avg= 0.0
        self._grade= None

    def get_hakbun(self):
        return self._hakbun

    def set_hakbun(self,value):
        self._hakbun = value

    hakbun = property(get_hakbun, set_hakbun)


    def get_irum(self):
        return self._irum

    def set_irum(self, value):
        self._irum = value

    irum = property(get_irum, set_irum)


    def get_kor(self):
        return self._kor

    def set_kor(self, value):
        self._kor=value

    kor= property(get_kor, set_kor)


    def get_eng(self):
        return self._eng
    def set_eng(self, value):
        self._eng=value
    eng=property(get_eng, set_eng)


    def get_math(self):
        return self._math
    def set_math(self, value):
        self._math=value
    math=property(get_math, set_math)


    def get_tot(self):
        return self._tot
    def set_tot(self,value):
        self._tot=value
    tot=property(get_tot, set_tot)

    def get_avg(self):
        return self._avg
    def set_avg(self,value):
        self._avg=value
    avg = property(get_avg, set_avg)

    def get_grade(self):
        return self._grade
    def set_grade(self, value):
        self._grade=value
    grade = property(get_grade, set_grade)

    def input_sungjuk(self):

        self._hakbun=input("학번을 입력해 주세요=>")
        self._irum=input("이름을 입력해 주세요=>")
        self._kor=int(input("국어 성적을 입력해 주세요=>"))
        self._eng=int(input("영어 성적을 입력해 주세요=>"))
        self._math=int(input("수학 성적을 입력해 주세요=>"))



    def process_sungjuk(self):

        self._tot= self._kor + self._eng + self._math
        self._avg=self._tot/3

        if self._avg>= 90:
            self._grade = "수"
        elif self._avg>= 80:
            self._grade = "우"
        elif self._avg>= 70:
            self._grade = "미"
        elif self._avg>= 60:
            self._grade = "양"
        else:
            self._grade = "가"

    def output_sungjuk(self):
        cnt = 0
        total_avg=0
        for row in dbcursor.execute('SELECT*FROM sungjuk order by hakbun asc'):
            print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
                (str(row[0]), str(row[1]), row[2], row[3],
                 row[4], row[5], row[6], row[7]))
            total_avg += row[6]
            cnt += 1
        print("         총학생수 = %d, 전체 평균= %.2f\n" % (cnt, total_avg / cnt))
