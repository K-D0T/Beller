from django import forms
from .models import ArtWork
from django.forms import widgets

class MainForm(forms.ModelForm):


	class Meta:
		model = ArtWork
		fields = '__all__'

		widgets = {
			'pic': FileInput(attrs={'image': 'image'})

		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for i in self.fields:

			self.fields[i].widget.attrs['class'] = 'form-control'

		
