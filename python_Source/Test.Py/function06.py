
def circle_area(radius, *pi, **info):
    for item in pi:
        area = item*(radius**2)
        print("반지름:",radius,"PI:",item,"면적:",round(area,2))

    for key in info:
        print(key,":",info[key])


if __name__=="__main__":
    circle_area(3, 3.14, 3.1415, line_color="파랑",area_color="노렁")
    print()
    circle_area(5,3.14,3.1415,polygon_name="원",value="면적")


