#TemplateView : URL에 맞춰 해당 템플릿 파일의 내용을 보여주는 뷰
from django.views.generic.base import TemplateView
# CreateView: 테이블의 레코드를 생성하기 위해 필요한 폼을 보여주고 폼의 입력을 받아 테이블의 레코드를 생성하는 뷰
from django.views.generic.edit import CreateView
# UserCreationForm : User 모델의 객체를 생성하기 위해 보여주는 뷰. 장고에서 기본으로 제공해주는 뷰
from django.contrib.auth.forms import UserCreationForm
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'


# 계정 생성 정의
class UserCreateView(CreateView):
    template_name = 'registration/register.html'    # 화면에 보여줄 템플릿 지정
    form_class = UserCreationForm   # 장고가 제공해주는 폼 사용
    # reverse_lazy는 reverse와 같은 기능인데 generic view에서는 reverse는 사용할 수 없고
    # reverse_lazy를 사용해야한다.
    # 'register_done'은 url.py에서 'accounts/register/done/' 경로에 대한 이름이고 해당 URL로 이동
    success_url = reverse_lazy('register_done')


# 'accounts/register/done/' URL을 처리해주는 뷰 정의(계정 생성후 보여줄 뷰)
class UserCreateDoneTV(TemplateView):
    # User 레코드 생성(사용자 가입) 완료 후, 사용자에게 보여줄 템플릿 파일명 지정
    template_name = 'registration/register_done.html'
