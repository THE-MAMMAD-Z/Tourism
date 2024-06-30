from django import forms
from .models import Contact , Place

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location']