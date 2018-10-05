from fighter import Fighter
from bomber import Bomber

def war_game(a):
    a.take_off()
    a.fly()
    a.attack()
    a.land()

if __name__ =="__main__":
    f15 = Fighter(3)
    war_game(f15)
    print()

    b29=Bomber(3)
    war_game(b29)

