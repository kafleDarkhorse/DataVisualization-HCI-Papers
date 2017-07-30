from django.db import models
from django.utils import timezone
# Create your models here.

class Data(models.Model):
	title = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.category