from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from content.models import Game, Movie, Book
from rest_framework.exceptions import ValidationError

from users.models import CustomUser


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    username = serializers.CharField(
        max_length=64,
        validators=...,
    )

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')

        user_by_email = CustomUser.objects.filter(email=email).first()
        user_by_username = CustomUser.objects.filter(username=username).first()

        error_msg = {}

        if user_by_email != user_by_username:
            if user_by_email:
                error_msg['email'] = (
                    'Этот адрес электронной почты уже '
                    'зарегистрирован, введите другой.'
                )
            if user_by_username:
                error_msg['username'] = (
                    'Это имя пользователя уже занято, введите другое.'
                )
            if user_by_email and user_by_username:
                error_msg['email'] = (
                    'Этот почтовый адрес электронной почты не '
                    'соответствует пользователю с таким именем.'
                )

        if error_msg:
            raise ValidationError(error_msg)

        return data


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        validators=(UnicodeUsernameValidator(),),
    )
    confirmation_code = serializers.CharField(
        required=True,
        allow_blank=False
    )

    def validate(self, data):
        username = data.get('username')
        confirmation_code = data.get('confirmation_code')

        user = get_object_or_404(CustomUser, username=username)

        if not default_token_generator.check_token(user, confirmation_code):
            raise ValidationError({'token': 'Неверный код подтверждения.'})

        return data


class GameSerializer(serializers.ModelSerializer):
  pass


class MovieSerializer(serializers.ModelSerializer):
  pass


class BookSerializer(serializers.ModelSerializer):
  pass
