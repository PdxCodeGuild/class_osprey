from django.shortcuts import render
from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer

class StudentAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()
    
class AddStudent(generics.CreateAPIView):
    serializer_class = StudentSerializer

class StudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentSearch(generics.ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        first_name = self.kwargs['first_name']
        return Student.objects.filter(last_name = first_name)