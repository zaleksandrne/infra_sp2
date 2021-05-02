import django_filters
from django.db.models import Avg
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import SAFE_METHODS

from .filters import TitleFilter
from .models import Category, Genre, Title
from .permissions import IsAdminOrReadOnly
from .serializers import (
    CategorySerializer, GenreSerializer, TitleSerializerRead,
    TitleSerializerWrite)


class BaseViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass


class TitleViewSet(BaseViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin):
    queryset = Title.objects.annotate(
        rating=Avg('titles__score')
    ).order_by('name')
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, ]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitleSerializerRead
        return TitleSerializerWrite


class GenreViewSet(BaseViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name', ]
    lookup_field = 'slug'


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name', ]
    lookup_field = 'slug'
