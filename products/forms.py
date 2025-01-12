
from django import forms
from .models import Review
from django.core.validators import EmailValidator

RATING_CHOICES = [
    (1, 'Very Satisfied'),
    (2, 'Satisfied'),
    (3, 'Neither Satisfied nor Dissatisfied'),
    (4, 'Dissatisfied'),
    (5, 'Very Dissatisfied'),
]
 
class AddReviewForm(forms.ModelForm):
    rate = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    content = forms.CharField(max_length=255, required=True)
    class Meta:
        model = Review
        fields = ['rate', 'content']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)