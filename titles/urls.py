from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router = DefaultRouter()

router.register('titles', TitleViewSet)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
urlpatterns = [
    path('titles/<int:title_id>/reviews/', include('reviews.urls')),
    path('', include(router.urls)),
]
