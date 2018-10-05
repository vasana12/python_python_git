import pickle
import os

class Sungjuk:
    def __init__(self):
        self._hakbun = None
        self._irum = None
        self._kor = 0
        self._eng = 0
        self._math = 0
        self._tot = 0
        self._avg = 0.0
        self._grade = None

    def input_sungjuk(self):
        self._hakbun = input("학번을 입력해 주세요=>")
        if self._hakbun == "exit":
            return True
        self._irum = input("이름을 입력해 주세요=>")
        self._kor = int(input("국어 성적을 입력해 주세요=>"))
        self._eng = int(input("영어 성적을 입력해 주세요=>"))
        self._math = int(input("수학 성적을 입력해 주세요=>"))
        return False

    def process_sungjuk(self):
        self._tot = self._kor + self._eng + self._math
        self._avg = self._tot / 3

        if self._avg >= 90:
            self._grade = "수"
        elif self._avg >= 80:
            self._grade = "우"
        elif self._avg >= 70:
            self._grade = "미"
        elif self._avg >= 60:
            self._grade = "양"
        else:
            self._grade = "가"

    def output_sungjuk(self):

        print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
              (self._hakbun, self._irum, self._kor, self._eng,
               self._math, self._tot, self._avg, self._grade))


if __name__ == '__main__':

    fp = open("binary.dat", "wb")
    while True:
        obj = Sungjuk()

        if obj.input_sungjuk():
            break

        obj.process_sungjuk()
        pickle.dump(obj,fp)
        print()

    # fp =open ("binary.dat", "rb")
    # lst=[]
    #
    # try:
    #     while True:
    #         obj = pickle.load(fp)
    #         lst.append(obj)
    # except:
    #     pass
    # finally:
    #     s = "성적표"
    #     print(s.center(47, "*"))
    #     print("=" * 50)
    #     print("\n학번     이름   국어   영어   수학   총점   평균   등급")
    #     print("=" * 50)
    #     for obj in lst:
    #         obj.output_sungjuk()
    #     print("=" * 50)

    fp = open("binary.dat", "rb")
    lst = []
    while True:
        if (fp.tell() == os.fstat(fp.fileno()).st_size):
            break
        obj = pickle.load(fp)
        lst.append(obj)
        s = "성적표"
        print(s.center(47, "*"))
        print("=" * 50)
        print("\n학번     이름   국어   영어   수학   총점   평균   등급")
        print("=" * 50)
        for obj in lst:
            obj.output_sungjuk()
        print("=" * 50)