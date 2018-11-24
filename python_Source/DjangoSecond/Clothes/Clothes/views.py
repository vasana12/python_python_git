#TemplateView : URL에 맞춰 해당 템플릿 파일의 내용을 보여주는 뷰
from django.views.generic.base import TemplateView
# CreateView: 테이블의 레코드를 생성하기 위해 필요한 폼을 보여주고 폼의 입력을 받아 테이블의 레코드를 생성하는 뷰
from django.views.generic.edit import CreateView
# UserCreationForm : User 모델의 객체를 생성하기 위해 보여주는 뷰. 장고에서 기본으로 제공해주는 뷰
from django.contrib.auth.forms import UserCreationForm
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'mainPage.html'
