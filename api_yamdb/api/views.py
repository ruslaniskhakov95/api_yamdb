from api.mixins import CategoryGengeMixin
from api.serializers import GenreSerializer
from reviews.models import Genre


class GenreViewSet(CategoryGengeMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
