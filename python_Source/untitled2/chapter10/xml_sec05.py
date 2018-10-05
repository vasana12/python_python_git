#-*-coding: utf-8 -*-
from xml.dom.minidom import parse

dom_doc=parse('movies.xml')
movies = dom_doc.getElementsByTagName('movie')
print(len(movies))
print("="*40)
for index in range(len(movies)):
    type = movies[index].getElementsByTagName('type')
    description = movies[index].getElementsByTagName('description')
    print("type:",type[0].firstChild.data)
    print("description:",description[0].firstChild.data)
    print("="*40)
