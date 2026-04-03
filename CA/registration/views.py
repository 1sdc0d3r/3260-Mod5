from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import RegistrationForm
from .models import Registration

def registration(req):
    if req.method == "POST":
        form = RegistrationForm(req.POST)

        if form.is_valid():
            print(form.cleaned_data)
            entry = Registration(name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message'])

            entry.save()
            return HttpResponseRedirect("/confirmation")

    else:
        form = RegistrationForm()

    return render(req, "registration/registration.html", {
        "form": form
    })


def callConfirmation(req):
    return render(req, "registration/confirmation.html")
