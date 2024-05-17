from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from api.filters import TitleFilter
from api.mixins import CategoryGengeMixin
from reviews.models import Genre, Title, Category, Review
from .serializers import (ReviewSerializer, GenreSerializer,
                          TitleSerializer, TitleGETSerializer,
                          CategorySerializer, CommentSerializer)
from users.permissions import (IsAuthorModeratorAdminOrReadOnly,
                               IsAdminOrReadOnly)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthorModeratorAdminOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            title_id=title.id,
            author_id=self.request.user.id
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthorModeratorAdminOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        review_id = self.kwargs.get('review_id')
        return title.reviews.get(id=review_id).comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(
            review_id=review.id,
            author_id=self.request.user.id
        )


class CategoryViewSet(CategoryGengeMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class GenreViewSet(CategoryGengeMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TitleGETSerializer
        return TitleSerializer
