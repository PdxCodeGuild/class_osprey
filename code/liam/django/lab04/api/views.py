from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer

# Create your views here.

class StudentAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class CreateStudent(generics.CreateAPIView):
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()