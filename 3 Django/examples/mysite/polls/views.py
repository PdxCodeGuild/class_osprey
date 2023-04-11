from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Question, Choice, Vote

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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        question = Question.objects.get(pk=self.kwargs['pk'])
        for choice in question.choice_set.all():
            votes = choice.vote_set.filter(voter=self.request.user)
            if len(votes) > 0:
                context['user_vote'] = votes.get(voter=self.request.user)
        return context


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

        for choice in question.choice_set.all():
            user_votes = choice.vote_set.filter(voter=request.user)
            if len(user_votes) > 0:
                old_vote = user_votes.get(voter=request.user)
                old_vote.choice = selected_choice
                old_vote.vote_date = timezone.now()
                old_vote.save()

                return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

        new_vote = Vote(voter=request.user, choice=selected_choice)
        new_vote.save()
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


@login_required
def add_question(request):
    try:
        new_q = Question(
            question_text=request.POST['question'], created_by=request.user)
        new_q.save()
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('polls:index'))


@login_required
def edit_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.created_by:
        return HttpResponseRedirect(reverse('polls:detail', args=(question_id,)))

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
