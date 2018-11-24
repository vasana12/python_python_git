from django.urls import path
from .views import *

app_name= 'choice'

urlpatterns = [
    path('choice',ChoiceLV.as_view(), name='index'),

]