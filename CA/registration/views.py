from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import RegistrationForm
# from .models import Registration

class RegistrationView(View):
    def get(self,req):
        form = RegistrationForm()

        return render(req, "registration/registration.html", {
            "form": form
        })

    def post(self,req):
        form = RegistrationForm(req.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect("/confirmation")
        return render(req, "registration/registration.html", {"form": form})

# def registration(req):
#     if req.method == "POST":

#         # form_email = req.POST['email']
#         # if len(Registration.objects.filter(email=form_email)):
#         form = RegistrationForm(req.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect("/confirmation")
#     else:
#         form = RegistrationForm()

#     return render(req, "registration/registration.html", {
#         "form": form
#     })


def callConfirmation(req):
    return render(req, "registration/confirmation.html")
