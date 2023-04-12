from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


# def index(request):
#     return HttpResponse("Hello, world. You're at the Chirp home.")


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"