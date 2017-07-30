from django import forms

from .models import Data

class DataForm(forms.ModelForm):

	class Meta:
		model = Data
		field = ('title', 'category', 'location')