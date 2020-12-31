from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import (
    DeletePost,
    PostList,
    PostDetail,
    PostListDetailFilter,
    AdminPostDetail,
    CreatePost,
    EditPost,
)

app_name = "blog_api"

router = DefaultRouter()
# router.register("", PostList, basename="post")


# urlpatterns = [path("", include(router.urls))]

urlpatterns = [
    path("posts/<slug:slug>/", PostDetail.as_view(), name="detailcreate"),
    path("", PostList.as_view(), name="listcreate"),
    path("search/", PostListDetailFilter.as_view(), name="post-search"),
    path("admin/create/", CreatePost.as_view(), name="createpost"),
    path(
        "admin/edit/postdetail/<int:pk>/",
        AdminPostDetail.as_view(),
        name="admindetailpost",
    ),
    path("admin/edit/<int:pk>/", EditPost.as_view(), name="editpost"),
    path("admin/delete/<int:pk>/", DeletePost.as_view(), name="deletepost"),
]