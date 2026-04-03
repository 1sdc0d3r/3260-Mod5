from django.urls import path

from . import views

urlpatterns = [
    path("", views.RegistrationView.as_view()),
    path("confirmation", views.callConfirmation),
    path("participants", views.ParticipantsView.as_view()),
    path(
        "participants/<int:pk>/edit",
        views.ParticipantUpdateView.as_view(),
        name="participant_edit",
    ),
    path(
        "participants/<int:pk>/delete",
        views.ParticipantDeleteView.as_view(),
        name="participant_delete",
    ),
]
