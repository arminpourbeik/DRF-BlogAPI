from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
    DjangoModelPermissions,
    IsAuthenticated,
)
from rest_framework import filters

from blog.models import Post
from .serializers import PostSerializer
from .permissions import PostUserWritePermission


# class PostList(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     serializer_class = PostSerializer

#     # Define custom queryset
#     def get_queryset(self):
#         return Post.objects.all()

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get("pk")
#         return get_object_or_404(Post, slug=item)


# class PostList(viewsets.ViewSet):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Post.post_objects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = (PostUserWritePermission,)
    queryset = Post.objects.all()

    lookup_field = "slug"


class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["^slug"]


class CreatePost(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class EditPost(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
