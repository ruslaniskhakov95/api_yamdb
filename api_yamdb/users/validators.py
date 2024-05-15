import re
from django.core.exceptions import ValidationError


def username_validator(value):
    if value == 'me':
        raise ValidationError('Имя "me" недопустимо для использования.')
    if not re.fullmatch(r'^[\w.@+-]+$', value):
        raise ValidationError('Имя пользователя не соответствует шаблону.')
    return value
