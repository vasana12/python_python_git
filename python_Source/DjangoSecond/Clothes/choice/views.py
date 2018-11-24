from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Bookmark
# Create your views here.

class ChoiceLV(ListView):
    model = Bookmark
    template_name = 'choice/choice_main.html'
    # ListView 를 상속받아 Post 클래스로부터 리스트를 리턴하는데 그 이름을 post