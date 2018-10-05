#-*-coding: utf-8 -*-
import xml.etree.ElementTree as et

tree = et.ElementTree(file='fruit.xml')
root = tree.getroot()
for s in root:
    print('tag:', s.tag, 'attributes:', s.attrib)
    for grandchild in s:
        print('\ttag:', grandchild.tag, 'attributes:',grandchild.attrib)

