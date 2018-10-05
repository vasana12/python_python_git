class CircleCalculator(object):

    @staticmethod
    def calculate_area(radius, pi):
        area = pi*(radius**2)
        return round(area,2)

    @staticmethod
    def calculate_circumference(radius, pi):
        circumference =2 * pi * radius
        return round(circumference,2)

if __name__=="__main__":
    print("반지름:",3, "면적:",CircleCalculator.calculate_area(3,3.14))
    print("반지름:",3, "둘레:",CircleCalculator.calculate_circumference(3, 3.14))

