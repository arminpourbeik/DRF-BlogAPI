from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    """
    Database table for posts
    """

    # Custom manager
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    OPTIONS = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.PROTECT,
        default=1,
    )
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    status = models.CharField(
        max_length=10,
        choices=OPTIONS,
        default="published",
    )

    objects = models.Manager()  # Default manager
    post_objects = PostObjects()  # Custom manager

    class Meta:
        ordering = ("-published",)

    def __str__(self) -> str:
        return self.title
