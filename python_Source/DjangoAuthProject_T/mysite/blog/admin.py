from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ['modify_date']
    search_fields = ('title', 'content')
    # 기사 내용에 대한 제목을 slug로 지정할 수 있다.
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Post, PostAdmin)