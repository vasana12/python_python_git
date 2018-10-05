import re
m_str = 'matches the start of a string.'
p = re.compile(r'\w+')
m=re.match(p,m_str);
r=re.search(p,m_str);
print(m)
print(r)