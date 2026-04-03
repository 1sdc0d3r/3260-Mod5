from random import choices
from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Registration(models.Model):
    full_name = models.CharField( max_length=20)
    email = models.EmailField(max_length=254, default="")
    contact_number = models.CharField(max_length=15, default="")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default="")

    dietary_choices = [('1', 'veggie'),('2', 'normal'),('3', 't-rex')]
    dietary = models.CharField(max_length=1, choices=dietary_choices, default='2')
