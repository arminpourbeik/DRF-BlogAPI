from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import PostList

app_name = "blog_api"

router = DefaultRouter()
router.register("", PostList, basename="post")


urlpatterns = [path("", include(router.urls))]
