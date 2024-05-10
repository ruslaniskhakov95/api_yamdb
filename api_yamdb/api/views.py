from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from api.filters import TitleFilter
from api.permissions import (IsAdminOrReadOnly,)
from api.serializers import (TitleSerializer, TitleGetSerializer,)
from reviews.models import Title


class TitleViewSet(viewsets.ModelViewSet):
    queryset = (
        Title.objects.all()
    )
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TitleGetSerializer
        return TitleSerializer
