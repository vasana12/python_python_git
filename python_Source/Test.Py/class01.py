class Test02:
    _b =100;
    def __m(self):
        return 'a'
    def k(self):
        print(self.__m() , self._b)

if __name__=='__main__':
    y=Test02()
    y.k()
    y._b=10
    print(y._b)
    print(Test02._b)
    #__ 는 compile 하면서 이름이 변경되기 때문에 접근 불가