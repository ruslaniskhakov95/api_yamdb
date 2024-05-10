from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ReviewViewSet

router_api_v1 = SimpleRouter()
router_api_v1.register(
    r'title/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')


urlpatterns = [
    path('', include(router_api_v1.urls)),
]
