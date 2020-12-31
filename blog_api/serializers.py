from rest_framework import serializers

from blog.models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post instance
    """

    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "author",
            "excerpt",
            "content",
            "status",
            "category",
            "slug",
        )