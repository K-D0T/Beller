from django.db import models


class SIZE(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class RequestPainting(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=500, null=True)
	email = models.EmailField(max_length=254)
	request = models.CharField(max_length=500, null=True)
	referencepicture = models.ImageField(upload_to='media', null=True, blank=True)
	size = models.ForeignKey(SIZE, on_delete=models.PROTECT, null=True)
	objects = models.Manager()
		


class ArtWork(models.Model):
	id = models.AutoField(primary_key=True)
	price = models.IntegerField()
	size = models.SlugField(default=0)
	about = models.CharField(max_length=500, null=True)
	picture = models.ImageField(upload_to='media', null=True)
	objects=models.Manager()
