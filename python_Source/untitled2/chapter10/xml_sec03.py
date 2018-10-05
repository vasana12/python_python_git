#-*-coding: utf-8 -*-
import sys
import xml.sax
from xml.sax.handler import ContentHandler

class MyHandler(ContentHandler):    #핸들러를 상속받는다.
    _movie_type = ['collection','movie' ,'type']     #엘리먼트 목록지정
    _movie_description = ['collection','movie','description']

    def __init__(self, writer = sys.stdout):    #표준 출력을 지정 및 초기화
        self._writer = writer
        self._node = []
        ContentHandler.__init__(self)

    def startElement(self, name, attrs):    #ContentHandler의 재정의 메소드(=오버라이딩한 메소드)
        self._node.append(name)

    def endElement(self,name):     #ContentHandler의 재정의 메소드
        self._node.pop()


    def characters(self, data):     #ContentHandler의 재정의 메소드
        if self._node == self. _movie_type:
            self._writer.write(u'type: %s\n' % data)
        elif self._node == self._movie_description:
            self._writer.write(u'description: %s\n' %data)
            self._writer.write(u"===============================\n")
    #위에 start~, end~, characters메소드들은 명시적으로 호출하는 명령문이 없어, 자동 호출됨 ->callback 메소드
    #시작 태그를 만나면, 종료 태그를 만나면, 데이터를 만나면 자동 호출됨

if __name__ == "__main__":
    parser = xml.sax.make_parser()      #SAX SMLReader 객체를 만들어 반환한다
    parser.setContentHandler(MyHandler())
    parser.parse("movies.xml")
