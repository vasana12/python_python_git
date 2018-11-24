"""mysite URL Configuration

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
from django.urls import path, include

from .views import HomeView
from .views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),

    # 장고는 /login/, /logout/으로 기본 경로가 정의되어 있다.
    # /accounts/login/로 경로를 지정하고 싶으면 /accounts/를 지정해주면 된다.
    path('accounts/', include('django.contrib.auth.urls')), #장고가 제공하는 인증 사용
    # 계정을 추가(생성)하는 뷰 url
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    # 계정 생성이 완료된 후 보여줄 뷰 url
    path('accounts/register/done', UserCreateDoneTV.as_view(), name='register_done'),

    path('', HomeView.as_view(), name='home'),

    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
]
