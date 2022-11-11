from django.urls import path, include
from .views import CommentListCreateView

urlpatterns = [
    path('<int:post_id>/list-create/', CommentListCreateView.as_view()),
]