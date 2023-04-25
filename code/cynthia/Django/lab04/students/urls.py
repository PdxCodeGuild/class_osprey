from django.urls import path

from . import StudentListView

urlpatterns = [ 
    path('', StudentListView.as_view(), name = 'home')
]