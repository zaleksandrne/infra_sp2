from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from titles.models import Title

from .models import Review
from .permissions import IsAuthorized
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorized, IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.titles.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=get_object_or_404(Title, id=self.kwargs.get('title_id'))
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorized, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
            title__id=self.kwargs.get('title_id'),
        )
        return review.reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=get_object_or_404(
                Review,
                id=self.kwargs.get('review_id'),
                title__id=self.kwargs.get('title_id'),
            )
        )
