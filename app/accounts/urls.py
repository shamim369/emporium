from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('registration/', views.SignUpView.as_view(), name='registration'),
    path('login/', views.SignInView.as_view(), name='login'),
]

# 127.0.0.1:8000/accounts/registration/
# 127.0.0.1:8000/accounts/login/