from django.db import models

# Create your models here.
class DjangoSungjuk(models.Model):#modles.Model 을 반드시 상속 받아 정의해야함.


    hakbun = models.CharField(max_length=10, primary_key=True)  # 작성안하면 자동으로 id 라는 이름으로 primary_key 생성됨
    irum = models.CharField(max_length=10, blank=True)
    kor = models.IntegerField(null=True, blank=True)
    eng = models.IntegerField(null=True, blank=True)  # 날짜를 다루기 위한 형식 년,월,일 널값 허용됨
    math = models.IntegerField(null=True, blank=True)
    tot = models.IntegerField(null=True, blank=True)
    avg = models.FloatField(null=True, blank=True)
    grade = models.CharField(max_length=4, blank=True, null=True)