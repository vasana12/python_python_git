class sungjuk:
    def __init__(self):
        self._hakbun = None
        self._irum = None
        self._kor =0
        self._eng =0
        self._math=0
        self._tot=0
        self._avg=0.0
        self._grade=None

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
        self.hakbun=input("학번을 입력해 주세요=>")
        self.irum=input("이름을 입력해 주세요=>")
        self.kor=int(input("국어 성적을 입력해 주세요=>"))
        self.eng=int(input("영어 성적을 입력해 주세요=>"))
        self.math=int(input("수학 성적을 입력해 주세요=>"))
        self.tot= self.kor + self.eng + self.math
        self.avg=self.tot/3


        if self.avg>= 90:
            self.grade = "수"
        elif self.avg>= 80:
            self.grade = "우"
        elif self.avg>= 70:
            self.grade = "미"
        elif self.avg>= 60:
            self.grade = "양"
        else:
            self.grade = "가"

    def output_sungjuk(self):
        s = "성적표"
        print(s.center(47, "*"))
        print("=" * 50)
        print("학번     이름   국어   영어   수학   총점   평균   등급")
        print("=" * 50)
        print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
              (self.hakbun, self.irum, self.kor, self.eng,
              self.math, self.tot, self.avg, self.grade))


if __name__=='__main__':
    test=sungjuk()
    test.input_sungjuk()
    test.output_sungjuk()