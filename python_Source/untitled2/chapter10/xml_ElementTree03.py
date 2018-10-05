#-*-coding: utf-8 -*-
import xml.etree.ElementTree as et

tree=et.ElementTree(file='fruit.xml')
root = tree.getroot()
print('root.tag:',root.tag)
print('root[0].tag:',root[0].tag)
print('root[0][0].tag:',root[0][0].tag)

for child in root:
    print('tag:',child.tag, 'attributes:', child.attrib, child.text)
    for gchild in child:
        print('\ttag:', gchild.tag, 'attributes:', gchild.attrib, gchild.text)
