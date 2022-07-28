from django.urls import path
from . import views
app_name = 'signup'
urlpatterns = [
    path('signup/',views. signup_func,name='signup'),
    path('login/',views. login_func,name='login'),
    path('logout/',views. logout_func,name='logout'),
]
