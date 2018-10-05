import re
str='''Spring
summer
fall
winter'''
c=re.compile('^.+',re.MULTILINE)
print(c.findall(str))