from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from blog.models import Post, Category


class PostTest(APITestCase):
    def test_view_posts(self):
        """Ensure we can get list of posts"""

        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.test_category = Category.objects.create(name="django")
        self.test_user01 = User.objects.create_user(
            username="test_user01",
            password="p@assw0rd",
        )
        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse("blog_api:listcreate")
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
