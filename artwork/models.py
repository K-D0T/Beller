from django.db import models

class ArtWork(models.Model):
	id = models.AutoField(primary_key=True)
	price = models.IntegerField()
	size = models.SlugField(default=0)
	about = models.CharField(max_length=500, null=True)
	picture = models.ImageField(upload_to='media', null=True)
	objects=models.Manager()
