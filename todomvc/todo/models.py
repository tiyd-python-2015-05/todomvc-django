from django.db import models

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length = 255)
    completed = models.BooleanField(default = True)
    order = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)
