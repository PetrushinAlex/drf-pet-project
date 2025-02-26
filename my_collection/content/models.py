from django.db import models

from content.validators import validate_release_date


class Game(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название игры',
        help_text='Введите название',
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
        help_text='Опишите игру',
    )

    year = models.SmallIntegerField(
        verbose_name='Дата выпуска',
        help_text='Укажите, когда вышла игра',
        validators=(validate_release_date,),
    )


class Movie(models.Model):
    pass


class Book(models.Model):
    pass
