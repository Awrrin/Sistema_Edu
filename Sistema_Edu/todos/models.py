from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=True)
    finished_at = models.DateField(null=True)
