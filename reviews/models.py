from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    title = models.ForeignKey(
        'titles.Title',
        on_delete=models.CASCADE,
        related_name='titles',
        verbose_name='Произведение',
    )
    text = models.TextField(
        verbose_name='Рецензия',
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='title_authors',
        verbose_name='Автор рецензии',
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Оценка',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации рецензии',
        db_index=True,
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'


class Comment(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Рецензия',
    )
    text = models.TextField(
        verbose_name='Комментарий',
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='comment_authors',
        verbose_name='Автор комментария',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации комментария',
        db_index=True,
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
