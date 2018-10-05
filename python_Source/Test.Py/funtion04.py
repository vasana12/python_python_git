#-*-coding:utf8 -*-

def circle_area(pi,*radius):
    areas=[]
    print(radius)
    for radius in radius:
        area =pi*(radius**2)
        areas.append(area)
    return areas
