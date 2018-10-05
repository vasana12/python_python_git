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

    def input_sungjuk(self, lst):
        while True:
            data = {}
            self._hakbun=input("학번을 입력해 주세요=>")
            if self._hakbun=="quit":
                break
            self._irum=input("이름을 입력해 주세요=>")
            self._kor=int(input("국어 성적을 입력해 주세요=>"))
            self._eng=int(input("영어 성적을 입력해 주세요=>"))
            self._math=int(input("수학 성적을 입력해 주세요=>"))

            data['hakbun']=self._hakbun
            data['irum'] = self._irum
            data['kor'] = self._kor
            data['eng'] = self._eng
            data['math'] = self._math
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
            data['tot']=self._tot
            data['avg']=self._avg
            data['grade']=self._grade

            lst.append(data)

    def output_sungjuk(self, lst):
        for data in lst:
            print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
                (data['hakbun'], data['irum'], data['kor'], data['eng'],
                 data['math'], data['tot'], data['avg'], data['grade']))

    def select_sungjuk(self,lst):
        hakbun=input("조회할 학번을 입력하세요=>")
        for data in lst:
            if data['hakbun']==hakbun:
                print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
                    (data['hakbun'], data['irum'], data['kor'], data['eng'],
                    data['math'], data['tot'], data['avg'], data['grade']))

    def update_sungjuk(self,lst):
        hakbun=input("업데이트할 학번을 입력하세요=>")
        for data in lst:
            if data['hakbun']==hakbun:
                data['hakbun']=input("수정할 학번 입력=>")
                data['irum']=input("수정할 이름 입력=>")
                data['kor']=input("수정할 국어 점수 입력=>")
                data['eng']=input("수정할 영어 점수 입력=>")
                data['math']=input("수정할 수학 점수 입력=>")
                print("업데이트 성공")
    def delete_sungjuk(self,lst):
        hakbun=input("삭제할 학번을 입력하세요=>")
        for data in lst:
            if data['hakbun']==hakbun:
                del data['hakbun']
                del data['irum']
                del data['kor']
                del data['eng']
                del data['math']
                del data['tot']
                del data['avg']
                del data['grade']
                print("삭제되었습니다.!")
if __name__=='__main__':

    test=Sungjuk()
    lst = []
    test.input_sungjuk(lst)
    s = "성적표"
    print(s.center(47, "*"))
    print("=" * 50)
    print("학번     이름   국어   영어   수학   총점   평균   등급")
    print("=" * 50)
    test.output_sungjuk(lst)
    print("="* 50)