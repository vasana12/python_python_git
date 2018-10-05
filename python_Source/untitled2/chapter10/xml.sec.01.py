#-*-coding:utf-8-*-
from xml.dom.minidom import parse, parseString

dom = parse('myfriend.xml') #DOM 객체로 리턴
#DOM 문서가 제공하는 getElementsByTagName 메소드로 name 엘리먼트 리턴
for name in dom.getElementsByTagName('name'):
    print(name.firstChild.data)

print("========")
datasource = open('myfriend.xml')
dom2=parse(datasource)
for name in dom.getElementsByTagName('addr'):
    print(name.firstChild.data)