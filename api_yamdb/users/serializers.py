from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import MyUser
from .validators import username_validator


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )


class GetTokenSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=150, required=True,)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'confirmation_code')


class SingUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True,
                                     validators=[username_validator])
    email = serializers.EmailField(max_length=254, required=True,)

    class Meta:
        model = MyUser
        fields = ('username', 'email')

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        if MyUser.objects.filter(username=username, email=email).exists():
            return data
        elif MyUser.objects.filter(username=username).exists():
            raise ValidationError(
                'Пользователь с таким именем уже существует'
            )
        elif MyUser.objects.filter(email=email).exists():
            raise ValidationError(
                'Пользователь с такой почтой уже существует'
            )
        return data
