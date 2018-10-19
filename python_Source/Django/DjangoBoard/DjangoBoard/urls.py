"""DjangoBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from board import views
urlpatterns = [
     url(r'^admin/', admin.site.urls),
    #^post/(\d+)/
    #^은 시작을 나타냄,
     url(r'^$', views.home), #path('실제경로', view 이름) ex=> path('',views.home)
     url(r'^writeForm/$', views.writeForm),                  #path('writeForm/',views.home) #^writeForm 으로 시작하고 /로 끝나야함
     url(r'^writeBoard/$', views.writeBoard),
     url(r'^viewBoard/$', views.viewBoard),
     url(r'^listPage/$', views.listPage),
     url(r'^updateForm/$', views.updateForm),
     url(r'^updateBoard/$', views.updateBoard),
     url(r'^deleteBoard/$', views.deleteBoard),
     url(r'^searchSubject/$', views.searchSubject),
     url(r'^listSearchPage/$', views.listSearchPage),
]
