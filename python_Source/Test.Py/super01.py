class MyScore:
    def __init__(self, kor, eng):
        self.kor =kor
        self.eng =eng
    def getTot(self):
        return (self.kor+self.eng)

class MyScore_Sub(MyScore):
    def __init__(self, kor, eng, math):
        self.math=math
        super().__init__(kor,eng)
    def getTot(self):
        return (str(super().getTot()+self.math))

if __name__ =='__main__':
    print(MyScore(57,67).getTot())
    print(MyScore_Sub(100,100,100).getTot())