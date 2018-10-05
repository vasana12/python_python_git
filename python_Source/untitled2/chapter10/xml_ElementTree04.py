#-*-coding: utf-8 -*-
import xml.etree.ElementTree as et

tree = et.ElementTree(file='fruit.xml')
root= tree.getroot()

for basket02 in root.iter('basket'): #iter() 전체목록을 리턴 한다.
    if basket02.attrib['classification'] =='vegetable':
        print('\t(채소)',basket02.attrib['name'])
    else:
        print('\t(과일)',basket02.attrib['name'])
