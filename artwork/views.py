from django.shortcuts import render
import requests
from .models import ArtWork, RequestPainting, SIZE
from .forms import * 
from django.http import HttpResponseRedirect
from django.urls import reverse
import smtplib, ssl
import re
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from django.contrib import messages

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


def RequestPaintings(request):
	if request.method == 'POST':
		form = RequestPaintingForm(request.POST, request.FILES)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			ID = post.id
			SendEmail(ID)
			messages.success(request, 'Thank you for submitting! ')
			return render(request, 'RequestPaintings.html', {'form': form})
		else:
			print(form.errors)
	else:
		form = RequestPaintingForm()

	return render(request, 'RequestPaintings.html', {'form': form})



def SendEmail(ID):

	name = list(RequestPainting.objects.filter(pk=ID).values('name'))
	name = name[0]['name']
	email = list(RequestPainting.objects.filter(pk=ID).values('email'))
	email = email[0]['email']
	referencepicture = list(RequestPainting.objects.filter(pk=ID).values('referencepicture'))
	referencepicture = referencepicture[0]['referencepicture']
	size = list(RequestPainting.objects.filter(pk=ID).values('size'))
	size = size[0]['size']
	size = list(SIZE.objects.filter(id=size).values())
	size = size[0]['name']
	request = list(RequestPainting.objects.filter(pk=ID).values('request'))
	request = request[0]['request']

	subject = ("Painting Request From: {}".format(name))
	body = "Request: "
	sender_email = "bshelleypaints@gmail.com"
	receiver_email = "bshelleypaints@gmail.com"
	password = "Reese2000"

	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject

	message.attach(MIMEText('{} \n \n Name: {} \n Email: {} \n Size: {} \n Request: {}'.format(body, name, email, size, request), "plain"))

	try:
		filename = ("/Users/Kaiden Thrailkill/Desktop/Environment/beller/beller/media/" + referencepicture)

		with open(filename, "rb") as attachment:
		    part = MIMEBase("application", "octet-stream")
		    part.set_payload(attachment.read())

		encoders.encode_base64(part)
		part.add_header(
		    "Content-Disposition",
		    f"attachment; filename= {filename}",

		)
		message.attach(part)
	except:
		pass

	
	text = message.as_string()
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login("bshelleypaints@gmail.com", "Reese2000")
	server.sendmail("bshelleypaints@gmail.com", "bshelleypaints@gmail.com", text)
	server.quit()
	
	

def contact(request):
	return render(request, 'contact.html')