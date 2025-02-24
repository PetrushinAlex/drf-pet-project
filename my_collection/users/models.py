from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""

    class Role(models.TextChoices):
        USER = 'user', _('Аутентифицированный пользователь')
        MODERATOR = 'moderator', _('Модератор')
        ADMIN = 'admin', _('Админ')

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Не более 150 символов.'
            'Только буквы, целые числа и @/./+/-/_.'
        ),
        validators=(UnicodeUsernameValidator()),
        error_messages={
            'unique': _('Пользователь уже существует.'),
        },
    )

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.USER,
        verbose_name='Уровень доступа пользователя',
    )

    bio = models.TextField(
        blank=True,
        verbose_name='Заметка о пользователе',
    )

    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта пользователя',
        help_text='Введите свой электронный адрес'
    )
