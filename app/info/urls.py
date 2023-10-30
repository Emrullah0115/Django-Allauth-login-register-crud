from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list", views.list, name="list"),
    path("create", views.create, name="create"),
    path("edit/<int:id>", views.edit , name="edit"),
    path("success-sign-out", views.logsuc , name="logsuc"),
    path("search", views.search, name="search"),
]
