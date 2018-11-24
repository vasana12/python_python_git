from django.db import models
#from test.pickletester import create_data
# Create your models here.

class DjangoBoard(models.Model):#modles.Model 을 반드시 상속 받아 정의해야함.

    id = models.IntegerField(primary_key=True) #작성안하면 자동으로 id 라는 이름으로 primary_key 생성됨
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank = True)
    created_date = models.DateField(null=True, blank=True) #날짜를 다루기 위한 형식 년,월,일 널값 허용됨
    email = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=200, blank=True)
    hits = models.IntegerField(null=True, blank=True)
