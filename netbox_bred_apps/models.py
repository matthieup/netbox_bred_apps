from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class OwnerChoices(ChoiceSet):
    key = "BredApplication.owner"

    CHOICES = [
        ("Infrastructure", "Infrastructure", ""),
        ("SaaS", "SaaS", ""),
        ("Wintel", "Wintel", ""),
        ("Network", "Network", ""),
    ]


class BredApplication(NetBoxModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    owner = models.CharField(max_length=100, choices=OwnerChoices)
    documentation = models.CharField(max_length=512)

    def get_absolute_url(self):
        return reverse("plugins:netbox_bred_apps:bredapplication", args=[self.pk])

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
