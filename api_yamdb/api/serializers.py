from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.constants import MAX_NAME_LENGTH
from reviews.models import Title
from reviews.validators import validate_year


class TitleGETSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=MAX_NAME_LENGTH
    )
    year = serializers.IntegerField(
        required=True,
        validators=(validate_year,),
    )
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')
        read_only_fields = ('id',)


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        required=False,
        many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        required=False,
        slug_field='slug',
    )

    class Meta:
        model = Title
        fields = ('name', 'year', 'description', 'genre', 'rating', 'category')

    def to_representation(self, value):
        return TitleGETSerializer(value).data
