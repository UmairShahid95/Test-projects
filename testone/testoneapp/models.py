from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Actor(models.Model):
        actorname = models.CharField(max_length=100)
        slug = models.SlugField()
        actor_email = models.EmailField(max_length=100, blank=True,null=True)
        actor_description = models.TextField(max_length=500, blank=True, null=True)
        thumbnail = models.ImageField(default= 'default.png',blank=True, null=True)
        author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING,blank=True, null=True)
        def __str__(self):
            return self.actorname
    
        def snippet(self):
            return self.actor_description[:50]+"..."