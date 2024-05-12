from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet, GetTokenView, SignUpView

app_name = 'api'

router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='users')


urlpatterns = [
    path('v1/auth/token/', GetTokenView.as_view(), name='get_token'),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
]