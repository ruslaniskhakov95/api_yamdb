from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from api.filters import TitleFilter
from api.mixins import CategoryGengeMixin
from api.permissions import (IsAdminOrReadOnly,)
from api.serializers import GenreSerializer, TitleSerializer, TitleGETSerializer, CategorySerializer
from reviews.models import Genre, Title, Category


class CategoryViewSet(CategoryGengeMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GenreViewSet(CategoryGengeMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


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
            return TitleGETSerializer
        return TitleSerializer
