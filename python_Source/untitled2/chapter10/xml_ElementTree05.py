#-*-coding: utf-8 -*-
import xml.etree.ElementTree as et

tree = et.ElementTree(file='fruit.xml')
root = tree.getroot()
for origin in root.findall('origin'):
    if origin.attrib['name']=='Andes': #origin 의 name 속성값이 Andes 라면
        origin.set('name','Canada') #속성값 변경을 Cananda 로 지정
    quantity = int(origin.find('quantity').text)
    price=int(origin.find('price').text)
    if quantity<5: #수량이 5이하인 origin 엘리먼트 삭제
        root.remove(origin)
    total = quantity*price
    for res in origin.findall('basket'):
        print(res.get('name'), format(total,',')) #목록과 (수량*단가) 금액을 출력

#변경된 내용을 파일로 출력한다.
tree.write("fruit_res.xml", encoding="utf-8", xml_declaration=True)