from django.urls import include, path

from api.views import GenreViewSet


v1_router.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
