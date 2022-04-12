from django.urls import path, reverse_lazy

from . import views

app_name = "unesco"
urlpatterns = [path("search/", views.Search.as_view(), name="search")]
