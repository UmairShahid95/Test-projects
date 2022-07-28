from django import forms
from . import models


class CreateActor(forms.ModelForm):
    class Meta:
        model = models.Actor
        fields = ['actorname', 'actor_email', 'actor_description', 'slug', 'thumbnail']