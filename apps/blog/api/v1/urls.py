from django.urls import path
from .views import CategoryListCreateView, TagListCreateView, BlogListCreateView, BlogRUDView

urlpatterns = [
    path('category-list-create/', CategoryListCreateView.as_view()),
    path('tag-list-create/', TagListCreateView.as_view()),
    path('blog-list-create/', BlogListCreateView.as_view()),
    path('blog-rud/<int:pk>/', BlogRUDView.as_view()),
]
