from django.urls import include, path

from api.views import TitleViewSet


v1_router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]