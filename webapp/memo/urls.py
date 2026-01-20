from django.urls import path
from . import views

urlpatterns = [
    path("", views.memo_home, name="memo_home"),
    path("new/", views.memo_create, name="memo_create"),
    path("hoge/", views.hoge_main, name="hoge_main"),
    path("<int:pk>/edit/", views.memo_update, name="memo_update"),
    path("<int:pk>/delete/", views.memo_delete, name="memo_delete"),
]