from rest_framework import serializers

from reviews.models import Review, User, Category, Genre, Title
from reviews.constants import MAX_NAME_LENGTH, MAX_SLUG_LENGTH
from reviews.validators import validate_year


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=MAX_NAME_LENGTH
    )
    slug = serializers.SlugField(
        required=True,
        max_length=MAX_SLUG_LENGTH,
        validators=[
            validators.UniqueValidator(queryset=Category.objects.all())
        ],
    )

    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=MAX_NAME_LENGTH
    )
    slug = serializers.SlugField(
        required=True,
        max_length=MAX_SLUG_LENGTH,
        validators=[
            validators.UniqueValidator(queryset=Genre.objects.all())
        ],
    )

    class Meta:
        model = Genre
        exclude = ('id',)


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
