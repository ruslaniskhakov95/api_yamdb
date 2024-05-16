from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CustomUserViewSet, GetTokenView, SignUpView

app_name = 'users'

router_api_v1 = SimpleRouter()
router_api_v1.register('users', CustomUserViewSet, basename='users')


urlpatterns = [
    path('auth/token/', GetTokenView.as_view(), name='get_token'),
    path('auth/signup/', SignUpView.as_view(), name='signup'),
    path('', include(router_api_v1.urls)),
]
