from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FeedbackForm
from .models import Feedback

#! Django Form Method 
def feedback(req):
    if req.method == "POST":
        form = FeedbackForm(req.POST)

        if form.is_valid():
            print(form.cleaned_data)
            feedback = Feedback(name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message'])
            feedback.save()
            return HttpResponseRedirect("/confirmation")

    else:
        form = FeedbackForm()

    return render(req, "feedback/feedback.html", {
        "form": form
    })

#! nonDjango Form Method - also valid
# def feedback(req):
#     if req.method == "POST":
#         field_name = req.POST['name']
#         field_email = req.POST['email']
#         field_message = req.POST['message']

#         if field_name == "" or len(field_message) < 10:
#             return render(req, "feedback/feedback.html", {
#                 "has_error": True
#             })
#         print(f'name: {field_name}\nemail: {field_email}\nmessage: {field_message}')
#         return HttpResponseRedirect("/confirmation")


#     # elif req.method == "GET":
#     return render(req, "feedback/feedback.html", {
#                 "has_error": False
#             })


def callConfirmation(req):
    return render(req, "feedback/confirmation.html")
