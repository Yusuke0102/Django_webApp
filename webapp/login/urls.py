from django.urls import path
from . import views

urlpatterns = [
    path("", views.Login_Home, name='login_home'),
]