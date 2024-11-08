from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("drafts/", views.DraftPostListView.as_view(), name="post_drafts"),
    path("archived/", views.ArchivedPostListView.as_view(), name="post_archived"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("new/", views.PostCreateView.as_view(), name="post_new"),
]