from django.db import models

# Create your models here.

class Todo(models.Model):
    # id
    # title - string, required
    # completed - boolean, default false
    # order - integer, not required, can be null
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True)