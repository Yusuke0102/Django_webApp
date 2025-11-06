from django.urls import path
from . import views

urlpatterns = [
    path("", views.Memo_hello, name='memo_home'),
]