from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import DayArchiveView, TodayArchiveView
from django.views.generic import FormView
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import PostSearchForm
from .models import Post

# Create your views here.

# # TemplateView
# class TagTV(TemplateView):
#     template_name = 'tagging/tagging_cloud.html'


# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    # ListView를 상속받아 Post클래스로부터 리스트를 리턴하는데 그 리스트의 이름을 posts로!
    context_object_name = 'posts'
    paginate_by = 2


# DetailView
class PostDV(DetailView):
    model = Post


# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    # modify_date의 연도를 기준으로 리스트 형태로 반환시켜줄 수 있는 부분
    # 꼭 date_field 아니어도 됨. 리스트 형태로 다 가져온다.
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    # modify_date의 월을 기준으로 리스트 형태로 반환시켜줄 수 있는 부분
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    # modify_date의 일을 기준으로 리스트 형태로 반환시켜줄 수 있는 부분
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


# FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        # __icontains 대소문자 구분해서 포함하는지 확인한다. / __contains는 대소문자 구분 안한다.
        # distinct() 중복을 제거한다.
        post_list = Post.objects.filter(Q(title__icontains=schWord) |
                                        Q(description__icontains=schWord) |
                                        Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    # slug는 별도의 입력을 받지 않겠다는 의미
    initial = {'slug':'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)


# 글 보는 것은 누구나 할 수 있지만 변경할 때는 로그인 했는지와 해당 user가 쓴 글을 가져와야한다.
class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    success_url = reverse_lazy('blog:index')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')