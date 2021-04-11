from django.db import models
from django.urls import reverse
# Create your models here.
class Animal(models.Model):
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField()
	found = models.DateTimeField(auto_now_add=True)
	ANIMALS = [
		(0, 'Unknown'),
		(1, 'Cat'),
		(2, 'Dog'),
		(3, 'Parrot')
	]
	atype = models.PositiveSmallIntegerField(default=0, choices=ANIMALS, verbose_name = "animal type")
	photo = models.ImageField()

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('show')