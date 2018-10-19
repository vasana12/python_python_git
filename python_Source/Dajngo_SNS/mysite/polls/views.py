from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Choice, Question

#--- Class-based View
class IndexView(ListView):
    template_name = 'polls/index.html'  #index.html 은 목적지
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


#--- Function-based View
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id) #Question 테이블 에서 qusetion_id 에 해당하는 객체 반환
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html',{
            'question':p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return an HttpResponseRedirect after successfully dealing
        #with POST data. This prevents data from being poseted twice if a
        #user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))