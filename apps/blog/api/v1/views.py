from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.db.models import Q
from ...models import Category, Tag, Blog
from .serializers import CategorySerializer, TagSerializer, BlogSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/v1/category-list-create/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/v1/tag-list-create/
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class BlogListCreateView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-list-create/
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    # permission_classes = [permissions.IsAuthenticated]


class BlogRUDView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-rud/<id>/
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class CategoryDeleteView(generics.DestroyAPIView):
    # http://127.0.0.1:8000/api/blog/category-delete/<id>/
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)





