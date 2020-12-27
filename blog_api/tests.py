from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from blog.models import Post, Category


class PostTest(APITestCase):
    def test_view_posts(self):
        """
        Ensure we can get list of posts
        """

        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        """
        Ensure we can create a post
        """

        self.test_category = Category.objects.create(name="django")
        self.test_user01 = User.objects.create_user(
            username="test_user01",
            password="p@assw0rd",
        )
        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse("blog_api:listcreate")
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        """
        Ensure a user can update their own post
        """

        self.test_category = Category.objects.create(name="django")
        self.test_user1 = User.objects.create_user(
            username="test_user",
            password="123456",
        )
        self.test_user2 = User.objects.create_user(
            username="test_user2",
            password="123456",
        )

        # Create test data for post
        test_post = Post.objects.create(
            category_id=1,
            title="Post title",
            excerpt="Post Excerpt",
            content="test content",
            slug="post-title",
            author_id=1,
            status="published",
        )
        self.client.login(username=self.test_user1.username, password="123456")

        post_id = Post.objects.get()

        url = reverse("blog_api:detailcreate", kwargs={"pk": post_id.id})
        response = self.client.put(
            url,
            {
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)