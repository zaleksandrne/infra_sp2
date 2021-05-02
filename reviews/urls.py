from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, ReviewViewSet

router = DefaultRouter()

router.register(r'', ReviewViewSet, basename='Reviews')
router.register(
    r'(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='Comments'
)

urlpatterns = [
    path('', include(router.urls)),

]
