from django.db import models


class ItemManager(models.Manager):
	def remove_completed(self):
		for item in self.all():
			if item.completed:
				item.delete()

	def get_active(self):
		return self.all().filter(completed=False)


# Create your models here.
class Item(models.Model):
	title = models.CharField(max_length=255)
	completed = models.BooleanField(default=False)
	order = models.IntegerField(null=True)

	objects = ItemManager()

	def toggle_complete():
		self.completed = not self.completed
