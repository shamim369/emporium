from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('registration/', views.sign_up, name='registration'),
    path('login/', views.sign_in, name='login'),
]