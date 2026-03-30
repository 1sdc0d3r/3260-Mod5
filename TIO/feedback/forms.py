from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20, error_messages={
        #* this isn't working for custom error_messages
        "required": "Your name must not be empty.",
        "max_length": "Please enter a shorter name."
    })
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=250, required=True)
