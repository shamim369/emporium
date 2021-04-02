from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

def sign_up(request):
    return JsonResponse({'RES': 'Registration'})
    
def sign_in(request):
    return JsonResponse({'RES': 'Login'})


