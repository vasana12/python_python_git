from xml.dom.minidom import parse

xmldoc = parse('items.xml')
itemlist = xmldoc.getElementsByTagName('dd')
print(len(itemlist))

for item in itemlist:
    print(item.attributes['name'].value) # name 으로 지정된 값 태그 안의 값 아니고