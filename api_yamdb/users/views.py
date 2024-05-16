from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, views, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import MyUser
from .permissions import IsAdmin
from .serializers import (CustomUserSerializer, GetTokenSerializer,
                          SingUpSerializer)


class CustomUserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = MyUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdmin,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(
        methods=['GET', 'PATCH'], detail=False,
        permission_classes=(IsAuthenticated,), url_path='me')
    def user_info(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PATCH':
            serializer = CustomUserSerializer(user, data=request.data,
                                              partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(role=user.role)
            return Response(serializer.data, status=status.HTTP_200_OK)


class SignUpView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SingUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email')
        username = request.data.get('username')
        user, created = MyUser.objects.get_or_create(
            email=email,
            defaults={'username': username}
        )
        token = default_token_generator.make_token(user)
        user.confirmation_code = token
        user.save()
        confirmation_message = f'Ваш код подтверждения {token}'
        send_mail(
            'Код подтверждения',
            confirmation_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetTokenView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        confirmation_code = serializer.validated_data.get('confirmation_code')
        user = get_object_or_404(MyUser, username=username)
        if confirmation_code != user.confirmation_code:
            return Response('Неверный код подтверждения',
                            status=status.HTTP_400_BAD_REQUEST)
        token = str(RefreshToken.for_user(user).access_token)
        return Response({'token': token}, status=status.HTTP_200_OK)
