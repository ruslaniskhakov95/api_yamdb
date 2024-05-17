from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import User
from .validators import username_validator


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )


class GetTokenSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=150, required=True,)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class SingUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True,
                                     validators=[username_validator])
    email = serializers.EmailField(max_length=254, required=True,)

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        if User.objects.filter(username=username, email=email).exists():
            return data
        elif User.objects.filter(username=username).exists():
            raise ValidationError(
                'Пользователь с таким именем уже существует'
            )
        elif User.objects.filter(email=email).exists():
            raise ValidationError(
                'Пользователь с такой почтой уже существует'
            )
        return data
