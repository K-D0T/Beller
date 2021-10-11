from django.shortcuts import render
import requests
from .models import ArtWork



def home(request):
	return render(request, 'home.html')

def artwork(request):
	data = list(ArtWork.objects.values())

	return render(request, 'artwork.html', {'data':data})

def ViewArtWork(request, id):
	data = list(ArtWork.objects.filter(pk=id).values())
	picture = data[0]['picture']
	price = data[0]['price']
	size = data[0]['size']
	about = data[0]['about']
	return render(request, 'ViewArtWork.html', {'picture':picture, 'price':price, 'size':size, 'about':about})
