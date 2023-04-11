from django.urls import path
from .views import SignUpView
from users import views

app_name = 'users'
urlpatterns = [
    # path("users/", views.index, name="users"),
    path("signup/", SignUpView.as_view(), name="signup"),
]

