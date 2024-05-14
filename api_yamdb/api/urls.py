from django.urls import include, path
from rest_framework.routers import SimpleRouter

app_name = 'api'

router_api_v1 = SimpleRouter()


urlpatterns = [
    path('api/v1/', include(router_api_v1.urls)),
]
