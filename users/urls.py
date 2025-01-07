from django.urls import path
from . import views as users_views

app_name = 'users'

urlpatterns = [

    path('register/', users_views.register, name = 'register'),
    path('profile', users_views.profile, name = 'profile'), 
] 