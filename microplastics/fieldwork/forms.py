from django import forms
from django.forms import ModelForm
from .models import Observation

class NameForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)


class ObservationForm(ModelForm):
    model = Observation
    fields = ['datetime', 'field_user', 'sample_type']


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)