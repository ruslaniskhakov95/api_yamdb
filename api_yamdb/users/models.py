from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import username_validator


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

    CHOICES = [
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
    ]

    username = models.CharField('username', max_length=150, unique=True,
                                validators=[username_validator])
    email = models.EmailField('email', max_length=254, unique=True,)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    bio = models.TextField('Биография', blank=True,)
    role = models.CharField('Роль', max_length=50, choices=CHOICES,
                            default=USER, blank=True,)
    confirmation_code = models.CharField(max_length=254, blank=True,)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_staff or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR
