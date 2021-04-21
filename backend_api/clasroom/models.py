from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.


class ClassRoom(models.Model):
    room_name = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User, related_name="created_by", on_delete=models.CASCADE
    )
    # unique_id = models.UUIDField(blank=False,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name
