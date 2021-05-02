from rest_framework import serializers

from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    def validate(self, data):
        reviews = Review.objects.filter(
            title=self.context.get('view').kwargs.get('title_id'),
            author=self.context.get('request').user
        ).exists()

        if reviews and self.context.get('request').method == 'POST':
            raise serializers.ValidationError('Отзыв существует')
        return data

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

        extra_kwargs = {
            'author': {'required': False},
            'title': {'required': False},
        }


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment

        extra_kwargs = {
            'pud_date': {'required': False},
            'review': {'required': False},
            'author': {'required': False},
        }
