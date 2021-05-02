from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=200,
                            unique=True,
                            verbose_name='Слаг')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='Жанр')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг')

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Название произведения'
                            )
    year = models.IntegerField(verbose_name='Год',
                               validators=[
                                   MinValueValidator(0),
                                   MaxValueValidator(datetime.now().year)]
                               )
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='titles',
                                 verbose_name='Категория'
                                 )
    genre = models.ManyToManyField(Genre,
                                   blank=True,
                                   related_name='genres',
                                   verbose_name='Жанр'
                                   )
    description = models.CharField(max_length=200,
                                   null=True,
                                   blank=True,
                                   verbose_name='Описание')

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
