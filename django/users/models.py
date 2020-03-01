from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # blank equals false because user might tell us their preference via line app only
    slug = models.SlugField(blank=False)
    # TODO: Change some values once the system design is decided
    nonce_for_line = models.CharField(
        verbose_name='nonce for linking line account',
        blank=True,
        null=True,
        max_length=50,
    )
    line_message_uid = models.CharField(
        verbose_name='message_uid to line the user',
        blank=True,
        null=True,
        max_length=50,
    )
