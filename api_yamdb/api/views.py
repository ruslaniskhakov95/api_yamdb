from api.mixins import CategoryGengeMixin
from api.serializers import CategorySerializer
from reviews.models import Category


class CategoryViewSet(CategoryGengeMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
