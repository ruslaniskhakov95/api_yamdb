from django.urls import include, path

from api.views import CategoryViewSet


v1_router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
