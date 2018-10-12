#visualstudio c++다운받고 라이브러리 konlpy설치, JPype1
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Okt   #Twitter
from collections import Counter

#http://kkma.snu.ac.kr/documents/index.jsp?doc=postag
#이 홈페이지 가서 라이브러리 내려받거ㄴㅏ

kkma = Kkma()   #중복되는 단어는 하나만 출력
twitter = Okt()

#nouns() : 명사 추출
print(kkma.nouns(u'명사만을 추출하여 워드클라우드를 그려봅니다. 명사만을 추출하여 워드클라우드를 그려봅니다'))
print(kkma.nouns(u'김하나는 밥을 많이 좋아합니다.김하나는 밥을 많이 좋아합니다.'))
print()

print(twitter.nouns(u'명사만을 추출하여 워드클라우드를 그려봅니다. 명사만을 추출하여 워드클라우드를 그려봅니다'))
print(twitter.nouns(u'김하나는 밥을 많이 좋아합니다.김하나는 밥을 많이 좋아합니다.'))
print()


#sentences():문장 추출
print(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
print()

#morphs(): 모든 품사의 형태소 추출
print(kkma.morphs(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))
print()

#pos(): 모든 품사의 형태소 추출과 품사 부착
print(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))
print()


"""

"""
