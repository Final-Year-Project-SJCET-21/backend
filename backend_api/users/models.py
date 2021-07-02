from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField

# from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

USER_CHOICES = (
    ("T", "Teacher"),
    ("A", "Administration"),
    ("S", "Student"),
)


class User(AbstractUser):
    """Default user for Backend API."""

    username = None
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    name = CharField(_("Name of User"), blank=True, max_length=255)

    email = EmailField(_("email address"), unique=True)
    role = CharField(max_length=1, choices=USER_CHOICES, default="S")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name


# class Teacher(models.Model):
#      user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name="teacher_account"
#     )

# class Student(models.Model):
#      user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name="student_account"
#     )
