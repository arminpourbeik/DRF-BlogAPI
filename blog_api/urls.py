from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import PostList, PostDetail, PostListDetailFilter

app_name = "blog_api"

router = DefaultRouter()
# router.register("", PostList, basename="post")


# urlpatterns = [path("", include(router.urls))]

urlpatterns = [
    path("posts/<int:pk>/", PostDetail.as_view(), name="detailcreate"),
    path("", PostList.as_view(), name="listcreate"),
    path("search/", PostListDetailFilter.as_view(), name="post-search"),
]