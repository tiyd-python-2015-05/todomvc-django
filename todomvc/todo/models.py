from django.db import models


class ItemManager(models.Manager):
	

# Create your models here.
class Item(models.Model):
	text = models.CharField(max_length=255)
	done = models.BooleanField(default=False)
	completed = models.BooleanField(default=False)
	selected = models.BooleanField(default=False)

	objects = ItemManager()
