import struct

if __name__=='__main__':
    intsize = struct.calcsize('i')
    floatsize = struct.calcsize('f')

    fp = open('binary.dat', 'rb')
    data= fp.read(intsize)          #int 타입 사이즈만큼 읽어들이겠다.
    num = struct.unpack('i',data)
    print(num)

    data = fp.read(floatsize)
    num= struct.unpack('f', data) #소수 6자리까지 유효숫자 나머지부터 쓰레기숫자
    print(num)

    fp.close()