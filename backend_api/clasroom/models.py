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


class EnrolledClass(models.Model):
    room = models.ForeignKey(ClassRoom, related_name="room", on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name="students", on_delete=models.CASCADE)
    enrollement_date = models.DateTimeField(auto_now_add=True, editable=False)


class Modules(models.Model):
    module_name = models.CharField(max_length=200)
    room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class ModuleFiles(models.Model):
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    filename = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    document = models.FileField(upload_to="module-notes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
