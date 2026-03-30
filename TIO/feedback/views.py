from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def feedback(req):
    if req.method == "POST":
        field_name = req.POST['name']
        field_email = req.POST['email']
        field_message = req.POST['message']
        print(f'name: {field_name}\nemail: {field_email}\nmessage: {field_message}')
        return HttpResponseRedirect("/confirmation")


    # elif req.method == "GET":
    return render(req, "feedback/feedback.html")


def callConfirmation(req):
    return render(req, "feedback/confirmation.html")
