from django.db import models

from reviews.constants import LIMIT_TEXT, MAX_NAME_LENGTH, MAX_SLUG_LENGTH


class Category(models.Model):
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        default='Категория отсутствует'
    )
    slug = models.SlugField(
        max_length=MAX_SLUG_LENGTH,
        unique=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.slug[:LIMIT_TEXT]
