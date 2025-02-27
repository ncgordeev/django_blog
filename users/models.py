from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ("user", "Пользователь"),
        ("author", "Автор"),
        ("admin", "Администратор"),
    )
    role = models.CharField(max_length=10, choices=ROLES, default="user")
    email = models.EmailField(unique=True)
