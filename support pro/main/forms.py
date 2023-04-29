from .models import *
from django import forms

class ticket_form(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'body', 'urgency']

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body':''}
        


