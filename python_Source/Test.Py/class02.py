# class Address:
#     name="Dominica"
#     addr ="seoul"
#     tel="02-111-111"
#
#
# print(Address.name, Address.addr, Address.tel) #클래스 변수 호출


# class Address:
#     def allPrn(self,name, addr,tel):
#         self.name=name
#         self.addr=addr
#         self.tel=tel
#         print(self.name, self.addr, self.tel)
#
# if __name__=='__main__':
#     addr01 =Address()
#
#     addr02=Address()
#     addr02.allPrn("Dominico", "Busan", "010-222-2222")


class Address:
    name ="Dominica"
    addr = "seoul"
    tel= "02-111-1111"

print(Address.name, Address.addr, Address.tel)
addr01 = Address()
addr02 = Address()
print(addr01.name, addr01.addr, addr01.tel)
addr01.name = "MBC"
print(addr01.name, addr01.addr, addr01.tel)
print(Address.name, Address.addr, Address.tel)