from django.db import models

# Create your models here.
class Todo(models.Model):
    # user = models.ForeignKey(User)
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    order = models.IntegerField(null=False)
