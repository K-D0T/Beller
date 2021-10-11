from django import forms
from .models import ArtWork, RequestPainting
from django.forms import widgets, FileInput, Textarea


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

class RequestPaintingForm(forms.ModelForm):


	class Meta:
		model = RequestPainting
		fields = '__all__'

		widgets = {
			'referencepicture': FileInput(attrs={'image': 'image'}),
			'request': Textarea(attrs={"rows":5, "cols":20}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for i in self.fields:

			self.fields[i].widget.attrs['class'] = 'form-control'

		self.fields['request'].widget.attrs['style'] = 'width: 500px;'
		self.fields['email'].widget.attrs['style'] = 'width: 300px;'
		self.fields['size'].widget.attrs['style'] = 'width: 100px;'
		self.fields['referencepicture'].requred = 'False'


