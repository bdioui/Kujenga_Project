from .models import Message
from django.forms import ModelForm
from django import forms

class message_form(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nom', 'prénom', 'email', 'message']