from django.db import models

from reviews.constants import LIMIT_TEXT, MAX_NAME_LENGTH, MAX_SLUG_LENGTH
from reviews.validators import validate_year


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_NAME_LENGTH,
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=validate_year
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        on_delete=models.SET_NULL,
        verbose_name='Slug жанра',
        blank=True

    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Slug категории',
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True
    )

    class Meta:
        default_related_name = 'titles'
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('year',)

    def __str__(self):
        return self.name[:LIMIT_TEXT]
