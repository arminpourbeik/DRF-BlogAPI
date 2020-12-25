from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import Post, Category


class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        test_category = Category.objects.create(name="django")
        test_user1 = User.objects.create_user(
            username="test_user01",
            password="p@assw0rd",
        )
        test_post = Post.objects.create(
            category_id=1,
            title="Post Title",
            excerpt="Post Excerpt",
            content="Post Content",
            slug="Post slug",
            author_id=1,
            status="published",
        )

    def test_blog_content(self):
        post = Post.post_objects.get()
        category = Category.objects.get()

        author = f"{post.author}"
        excerpt = f"{post.excerpt}"
        title = f"{post.title}"
        content = f"{post.content}"
        status = f"{post.status}"

        self.assertEqual(author, "test_user01")
        self.assertEqual(title, "Post Title")
        self.assertEqual(excerpt, "Post Excerpt")
        self.assertEqual(content, "Post Content")
        self.assertEqual(status, "published")

        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(category), "django")
