#레퍼런스 사이트 : https://dics.python.org/3/library/struct.html

import struct

struct_fmt = '=16s2fi' #char[16], float[2], int
struct_len = struct.calcsize(struct_fmt) # struct.calsize() : struct_fmt 를 처리한 크기를 구함

cities = []
with open('cities.dat', "rb") as file:
    while True:
        buffer = file.read(struct_len) # struct_len 값 만큼 읽어서 bytes 타입의 객체로 반환
        if not buffer: #파일의  끝에 도달하면 루프를 탈출한다.
            break
        city = struct.unpack(struct_fmt, buffer)
        cities.append(city)
        #if (file.tell()==os.fstat(file.fileno()).st_size): # 해당 파일에 대한 총 크기 구함 => 현재파일 크기가 tell 사이즈와 같다 = 더이상 읽을 내용이 없다.
        #   break
    for city in cities:
        name = city[0].decode(encoding='utf-8').replace('Wx00', '')
        print('City:{0}, Lat/Long:{1}/{2}, Population:{3}'.format(
            name,
            city[1],
            city[2],
            city[3]))