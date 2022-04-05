from django.urls import path, reverse_lazy

from . import views

app_name = "ads"
urlpatterns = [
    path("", views.ForumsListView.as_view(), name="all"),
    path("ad/<int:pk>", views.ForumDetailView.as_view(), name="ad_detail"),
    path(
        "ad/create",
        views.ForumsCreateView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_create",
    ),
    path(
        "ad/<int:pk>/update",
        views.ForumsUpdateView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_update",
    ),
    path(
        "ad/<int:pk>/delete",
        views.ForumsDeleteView.as_view(success_url=reverse_lazy("ads:all")),
        name="ad_delete",
    ),
    path("ad_picture/<int:pk>", views.stream_file, name="ad_picture"),
    path(
        "ad/<int:pk>/comment",
        views.CommentCreateView.as_view(),
        name="ad_comment_create",
    ),
    path(
        "comment/<int:pk>/delete",
        views.CommentDeleteView.as_view(success_url=reverse_lazy("ads")),
        name="ad_comment_delete",
    ),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
