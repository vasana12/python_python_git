#-*-coding:utf8 -*-
import re

m_str = "matches the start of a string."
m= re.match('[a-z]+',m_str);
r= re.search('[a-z]+',m_str);
print(re.search(".","\n"))
print(m)
print(r)

m_str = " matches the start of a string,"
p=re.compile('[a-z]+')
m= re.match(p,m_str);
r= re.search(p,m_str);
print(m)
print(r)

m_str = " mastewrasfsdfdsf"
m= re.match('[a-z]+',m_str);
r= re.search('[a-z]+',m_str);
print(m)
print(r)

