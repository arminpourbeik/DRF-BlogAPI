from rest_framework import generics
from rest_framework.permissions import (
    DjangoModelPermissions,
)

from blog.models import Post
from .serializers import PostSerializer
from .permissions import PostUserWritePermission


class PostList(generics.ListCreateAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer
    permission_classes = (DjangoModelPermissions,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostUserWritePermission,)
