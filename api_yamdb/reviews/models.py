from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from reviews.constants import (
    LIMIT_TEXT, MAX_NAME_LENGTH, MAX_SLUG_LENGTH, SCORE_MIN, SCORE_MAX
)
from reviews.validators import validate_year


User = get_user_model()


class BaseModel(models.Model):
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        default='Пусто',
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=MAX_SLUG_LENGTH,
        unique=True,
        verbose_name='Слаг'
    )

    class Meta:
        abstract = True
        verbose_name = 'Базовая модель'


class BasePublicationModel(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        abstract = True
        verbose_name = 'Базовая модель публикаций'


class Category(BaseModel):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.slug[:LIMIT_TEXT]


class Genre(BaseModel):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.slug[:LIMIT_TEXT]


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_NAME_LENGTH,
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска',
        validators=validate_year,
        db_index=True
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
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


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Название произведения',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Жанр произведения',
    )

    class Meta:
        verbose_name = 'Произведение - Жанр'
        verbose_name_plural = 'Произведение - Жанр'
        ordering = ['title__name']

    def __str__(self):
        return f'Произведение {self.title_id} - Жанр {self.genre_id}'


class Review(BasePublicationModel):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(SCORE_MIN),
            MaxValueValidator(SCORE_MAX)
        ],
        verbose_name='Оценка'
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'), name='unique_title_review'
            )
        ]

    def __str__(self):
        return self.text[:LIMIT_TEXT]


class Comment(BasePublicationModel):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:LIMIT_TEXT]
