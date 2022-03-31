from django.urls import path, reverse_lazy

from . import views

app_name = "ads"
urlpatterns = [
    path("", views.AdsListView.as_view(), name="all"),
    path("ad/<int:pk>", views.AdsDetailView.as_view(), name="ad_detail"),
    path(
        "ad/create",
        views.AdsCreateView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_create",
    ),
    path(
        "ad/<int:pk>/update",
        views.AdsUpdateView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_update",
    ),
    path(
        "ad/<int:pk>/delete",
        views.AdsDeleteView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_delete",
    ),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
