from django.contrib import admin

from .models import Question, Choice

#class ChoiceInline(admin.StackedInline): #각 필드를 쌓아서 보여줌
class ChoiceInline(admin.TabularInline): # 테이블 형식으로 보여줌 question 테이블 안에 choice 테이블 같이 보여줌
    model = Choice
    extra = 3       #편집할 데이터 갯수3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}), #필드 추가하고 싶으면 여기다가 더 넣으면 됨
        #('Date Information', {'fields': ['pub_date']}),
        ('Date Information' , {'fields': ['pub_date'], 'classes': ['collapse']}) #토글방식

    ]
    inlines = [ChoiceInline]
    list_display=('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
