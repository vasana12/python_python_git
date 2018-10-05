from datetime import date # 모듈을 임포트 한다.
#date 의 today() 메소드를 호출하게 되면 시스템이 가진 오늘 날짜를 리턴
d= date.today()
print(d.isoformat()) #년도 네 자리, 월, 일 두 자리 표현식을 적용
print(d.ctime()) # 시스템에 가진 오늘 날짜의 시간을 리턴
print(d.strftime("%y/%m/%d")) # ()안에 서식에 맞게 문자열로 적용하여 리턴