from django.db import models


class ConfirmationCode(models.Model):
    email = models.EmailField(
        unique=True,
        db_index=True
    )
    confirmation_code = models.CharField(
        max_length=255,
        null=True
    )

    class Meta:
        verbose_name = 'confirmation_code'
        verbose_name_plural = 'confirmation_codes'
