def sungjuk_input():
    lst = []

    while True:
        dict = {}

        dict["hakbun"] = input("학번 입력=>")
        if dict["hakbun"]=="exit":
            break
        dict['irum']=input("이름 입력=>")
        dict['kor']=int(input("국어점수 입력=>"))
        dict['eng']=int(input("영어점수 입력=>"))
        dict['math']=int(input("수학점수 입력=>"))
        dict['total']=dict.get('kor')+dict.get('eng')+dict.get('math')
        dict['avg']=dict.get('total')/3

        if dict.get('avg') >=90:
            dict['grade']="수"
        elif dict.get('avg') >=80:
            dict['grade'] = "우"
        elif dict.get('avg') >=70:
            dict['grade'] = "미"
        elif dict.get('avg') >=60:
            dict['grade'] = "양"
        else:
            dict['grade'] = "가"

        lst.append(dict)

        return lst