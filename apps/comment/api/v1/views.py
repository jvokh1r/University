from rest_framework import status, views, generics
from rest_framework.response import Response
from ...models import Comment
from .serializers import CommentSerializer
from apps.blog.models import Blog


class CommentListCreateView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/comment/v1/<post_id>/list-create/
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'post_id'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        print(self.lookup_url_kwarg)
        post_id = self.kwargs.get(self.lookup_url_kwarg)
        print(post_id)
        qs = qs.filter(post_id=post_id)
        print(qs)
        return qs


