
from django.shortcuts import redirect, render
from .models import Actor
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def actor_list(request):
    actor_list = Actor.objects.all()
    
    return render(request, 'actor_list.html', {'actor_list': actor_list})

def actor_description(request, slug):
    actor = Actor.objects.get(slug=slug)
    return render(request, 'actor_description.html', {'actor': actor})


@login_required(login_url='signup:login')
def actor_create(request):
    if request.method == 'POST':
      form = forms.CreateActor(request.POST, request.FILES)
      if form.is_valid():
          #save article to database
          Instance = form.save(commit='False')
          Instance.author = request.user
          Instance.save()
          
          return redirect('testoneapp:actor_list')
    else:
        form = forms.CreateActor
    return render(request, 'actor_create.html', {'form': form})