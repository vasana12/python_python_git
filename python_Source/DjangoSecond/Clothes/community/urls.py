from django.urls import path
from .views import *

app_name= 'community'

urlpatterns = [
    path('community',HomeView.as_view(), name='index'),
]