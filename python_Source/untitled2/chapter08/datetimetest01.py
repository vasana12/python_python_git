from datetime import date # 모듈을 임포트 한다.

d=date(2018,9,12) #년도, 월, 일의 객체를 생성
print(d) #객체 값을 리턴
print(d.isoweekday()) #월요일은 1부터
print(d.toordinal())#1월1일 이후로 date 객체까지 누적된 날짜를 반환
print(d.year, d.month, d.day) #속성값을 리턴
print(d.timetuple())#타입 객체로 속성값을 전체 리턴