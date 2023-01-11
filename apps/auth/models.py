from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.BinaryField(max_length=60)
    email = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.username} ({self.pk})"
