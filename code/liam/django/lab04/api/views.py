from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer

# Create your views here.

class StudentAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentSearch(generics.ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        queryset = Student.objects.all()
        name = self.request.query_params.get('first_name')
        if name is not None:
            queryset = queryset.filter(first_name__icontains=name)
        return queryset

class CreateStudent(generics.CreateAPIView):
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()