from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# 슬러그(slug): 페이지나 포스트를 설명하는 핵심단어의 집합을 의미하며 신문이나 잡지등에서
# 제목을 쓸 때 중요한 의미를 포함하는 단어만을 사용해서 제목을 작성하는 방법을 말한다.
# 웹에서는 URL로 사용함으로써 검색엔진에서 더 빨리 페이지를 찾아주고 검색엔진의 정확도를
# 높여준다.
# SlugField : unique 옵션을 추가해 검색시 기본키 대신 사용
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'post' # 테이블의 단수 별칭
        verbose_name_plural = 'posts' # 테이블의 복수 별칭
        db_table = 'blog_posts' # 저장될 테이블의 이름을 blog_posts로 지정
        ordering = ['-modify_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True) # allow_unicode=True:슬러그에 한글 사용 허용
        super(Post, self).save(*args, **kwargs)
