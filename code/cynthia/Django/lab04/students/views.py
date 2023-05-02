from django.shortcuts import render
from django.views.generic import ListView
from .models import Student


class StudentListView(ListView):
    model = Student
    template = 'student_list.html'