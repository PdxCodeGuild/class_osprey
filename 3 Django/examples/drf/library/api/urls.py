from django.urls import path
from .views import *

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('new/', CreateBook.as_view()),
    # path('<int:pk>/', BookDetailView.as_view()),
    # path('<int:pk>/update/', BookUpdateView.as_view()),
    # path('<int:pk>/delete/', BookDeleteView.as_view()),
    path('<int:pk>/', BookView.as_view()),
]
