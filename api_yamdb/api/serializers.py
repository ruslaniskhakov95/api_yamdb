from rest_framework import serializers, validators

from reviews.constants import MAX_NAME_LENGTH, MAX_SLUG_LENGTH
from reviews.models import Genre


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
