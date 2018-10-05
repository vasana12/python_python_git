class Car:
    def __init__(self):
        self._price = 0
        self._speed = 0
        self._color = None

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price =value
    price =property(get_price, set_price)

    def get_speed(self):
        return self._speed
    def set_speed(self, value):
        self._speed = value
    speed = property(get_speed, set_speed)

    def get_color(self):
        return self._color
    def set_color(self, value):
        self._color =value
    color = property(get_color, set_color)

if __name__ =="__main__":
    test = Car()
    test.price=2000
    print(test.price)
    test.speed=50
    print(test.speed)
    test.color="red"
    print(test.color)