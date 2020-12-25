from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post instance
    """

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "author",
            "excerpt",
            "content",
            "status",
        )