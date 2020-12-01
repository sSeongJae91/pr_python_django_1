from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from polls.models import Choice, Question

import logging

logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    logger.info("LOGGER TEST!!!")

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# -- function based View
def vote(request, question_id):
    logger.debug("vote().question_id: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1   #choice의 vote 객체 +1
        selected_choice.save()      #변경 사항을 choice테이블에 저장
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #리다이렉션

