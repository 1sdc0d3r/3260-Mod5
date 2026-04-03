from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        # fields = []
        fields = "__all__"
        # exclude = ['field_name']
        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'contact_number': 'Phone',
        }
        # error_messages={
        #     "required": "Your name must not be empty.",
        #     "max_length": "Please enter a shorter name."
        # }
