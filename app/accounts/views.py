from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class HomeView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class SignUpView(APIView):
    def post(self, request):
        name = request.data
        print(name)
        return Response(name)


class SignInView(APIView):

    def get(self, request):
        return Response({'RES': 'Login get'})

    def post(self, request):
        return Response({'RES': 'Login post'})


