from django import forms
from django.core.exceptions import ValidationError

from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        # exclude = ['field_name']
        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'contact_number': 'Phone',
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        query = Registration.objects.filter(email=email)
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
        if query.exists():
            raise ValidationError("That email is already registered.")
        return email
