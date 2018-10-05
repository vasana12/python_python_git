#-*-coding: utf-8 -*-
from xml.dom.minidom import parseString

test='''<?xml version="1.0" encoding="UTF-8"?>
<collection>
    <movie title="Enemy Behind">
       <type>War, Thriller</type>
       <format>DVD</format>
       <year>2003</year>
       <rating>PG</rating>
       <stars>10</stars>
       <description>Talk about a US-Japan war</description>
    </movie>
    <movie title="Transformers">
       <type>Anime, Science Fiction</type>
       <format>DVD</format>
       <year>1989</year>
       <rating>R</rating>
       <stars>8</stars>
       <description>A schientific fiction</description>
    </movie>
       <movie title="Trigun">
       <type>Anime, Action</type>
       <format>DVD</format>
       <episodes>4</episodes>
       <rating>PG</rating>
       <stars>10</stars>
       <description>Vash the Stampede!</description>
    </movie>
    <movie title="Ishtar">
       <type>Comedy</type>
       <format>VHS</format>
       <rating>PG</rating>
       <stars>2</stars>
       <description>Viewable boredom</description>
    </movie>
</collection>
'''

dom_doc = parseString(test)     #xml 문서가 파일이 아니라 텍스트 형식으로(string) 형식으로 돼 있을 때
movies = dom_doc.getElementsByTagName('movie')
print(len(movies))
for index in range(len(movies)):
    type = movies[index].getElementsByTagName('type')
    description = movies[index].getElementsByTagName('description')
    print(type[0].firstChild.data, " : ", description[0].firstChild.data)
