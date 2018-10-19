from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),# '/polls/  ex)경로가 :8000/polls/가 주어졌을때
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #/polls/5/    #parameter 로 pk로 정의되어있는 id 를 받음 ex):8000/polls/1/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), #/polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # /polls/5/vote/
]