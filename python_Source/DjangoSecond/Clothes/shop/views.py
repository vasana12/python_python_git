from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'shop/shop_main.html'
