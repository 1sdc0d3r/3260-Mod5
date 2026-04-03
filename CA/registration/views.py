from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView, DeleteView

from .forms import RegistrationForm
from .models import Registration

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

class ParticipantsView(View):
    def get(self,req):
        people = Registration.objects.all()
        return render(req, "registration/participants.html", {"people": people})


class ParticipantUpdateView(UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = "registration/editParticipant.html"
    success_url = "/participants"

class ParticipantDeleteView(DeleteView):
    model = Registration
    template_name = "registration/deleteConfirmation.html"
    success_url = "/participants"


def callConfirmation(req):
    return render(req, "registration/confirmation.html")
