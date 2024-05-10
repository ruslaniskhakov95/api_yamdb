from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from reviews.models import Title
from .serializers import ReviewSerializer
from .permissions import IsAuthorOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(
            title_id=title.id,
            author_id=self.request.user.id
        )
