from rest_framework import filters, status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from api.filters import TitleFilter
from api.permissions import (IsAdminOrReadOnly,)
from reviews.models import Title

from api.serializers import (TitleSerializer, TitleGetSerializer,)


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
