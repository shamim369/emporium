from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class SignUpView(APIView):

    def get(self, request, *args, **kwargs):
        name = request.data
        print(name)
        return Response(name)

    def post(self, request):
        return Response({'RES': 'Registration post'})


class SignInView(APIView):

    def get(self, request):
        return Response({'RES': 'Login get'})

    def post(self, request):
        return Response({'RES': 'Login post'})


