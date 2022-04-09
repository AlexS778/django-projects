from django.urls import path, reverse_lazy

from . import views

app_name = "autograder"
urlpatterns = [
    path("", views.mainview.as_view(), name="main"),
]
