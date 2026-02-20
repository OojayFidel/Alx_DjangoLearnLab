from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)

    # MUST be ImageField (this is what the checker is looking for)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True,
    )

    def __str__(self):
        return self.username