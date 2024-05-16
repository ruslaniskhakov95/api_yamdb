from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (ReviewViewSet, TitleViewSet, GenreViewSet,
                    CategoryViewSet, CommentViewSet)


router_api_v1 = SimpleRouter()

router_api_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
    )
router_api_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
    )
router_api_v1.register('titles', TitleViewSet, basename='titles')
router_api_v1.register('genres', GenreViewSet, basename='genres')
router_api_v1.register('categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('', include(router_api_v1.urls)),
]
