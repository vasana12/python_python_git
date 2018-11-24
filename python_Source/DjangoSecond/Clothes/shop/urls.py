from django.urls import path
from .views import *

app_name= 'shop'

urlpatterns = [
    path('shop',HomeView.as_view(), name='index'),
]