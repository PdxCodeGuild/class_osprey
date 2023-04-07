from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# def index(request):
#     question_list = Question.objects.all()
#     # output = ', '.join([q.question_text for q in question_list])
#     return render(request, 'polls/index.html', {'question_list': question_list})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'
    # model = Question

    def get_queryset(self):
        return Question.objects.all()


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


def add_question(request):
    new_q = Question(question_text=request.POST['question'])
    new_q.save()
    return HttpResponseRedirect(reverse('polls:index'))


def edit_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        # choice_text = request.POST['new_choice']
        # new_choice = Choice(question=question, choice_text=choice_text)
        # new_choice.save()

        try:
            if request.POST['new_q_text'] != question.question_text:
                question.question_text = request.POST['new_q_text']
                question.save()
        except KeyError:
            pass
        try:
            if request.POST['new_choice']:
                question.choice_set.create(
                    choice_text=request.POST['new_choice'])
        except KeyError:
            pass

    return render(request, 'polls/edit.html', {'question': question})
