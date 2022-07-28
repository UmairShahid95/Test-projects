from django.urls import path
from . import views
app_name = 'testoneapp'
urlpatterns = [
    path('', views.actor_list, name='actor_list'),
    path('create/', views.actor_create, name='actor_create'),
    path('<slug:slug>/', views.actor_description, name = 'actor_description'),
    
]
