from django.db import models

from content.validators import validate_release_date


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Введите название жанра',
    )
    slug = models.SlugField(
        max_length=28,
        unique=True,
        verbose_name='Идентификатор',
        help_text='Введите идентификатор жанра',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f"Genre: {self.name} (slug: {self.slug})"


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
