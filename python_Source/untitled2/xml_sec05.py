#-*-coding: utf-8 -*-
from xml.dom.minidom import parse

dom_doc=parse('movies.xml')
movies = dom_doc.getElementsByTagName('movies')
print(len(movies))
for index in range(len(movies)):
    type = movies[index].getElementsByTagName('type')
    description = movies[index].getElementsByTagName(description)
    print(type[0].firstChild.data, " : ", description[0].firstChild.data)
