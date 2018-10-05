#-*-coding: utf-8 -*-
import xml.etree.ElementTree
friend = xml.etree.ElementTree.parse('myfriend.xml')
friends = friend.findall("address")
for res in friends:
    print(res.find("name").text,",",res.find("addr").text)
print('====================')

for r in friend.getiterator(tag="name"):
    print(r.text)
for r in friend.getiterator(tag="addr"):
    print(r.text)
