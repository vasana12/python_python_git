import struct

if __name__ == '__main__':
    fp= open('binary.dat', 'wb')
    data = struct.pack('i',1)
    fp.write(data)
    data = struct.pack('f', 3.14)
    fp.write(data)
    fp.close()