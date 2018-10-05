import random
# lst=[]
# for i in range(1,46):
#     lst.append(i)
# print(lst)
# a=random.sample(lst,6)
# print(a)
# lst=[]
# loto_list=[]
# loto=0
# if loto==0:
#     for i in range(1,46):
#         lst.append(i)
#     while i<=5:
#         loto_list.append(lst.pop())
#         del loto_list
#         i+=1
#     loto=1
# elif loto==1:
#     for i in range(1,46):
#         lst.append(i)
#
# b=random.choice(lst)
# print(b)
def get_lotto_numbers():
    lotto_numbers= []
    while True:
        if len(lotto_numbers) == 6:
            break

        number = random.randint(1, 45)

        if number in lotto_numbers:
            continue
        else:
            lotto_numbers.append(number)

    return sorted(lotto_numbers)
if __name__=='__main__':
    lotto_numbers = get_lotto_numbers()
    print(lotto_numbers)