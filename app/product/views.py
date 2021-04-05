from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CategoryView(APIView):

    def get(self, request):
        content = {'message': 'Hello, Product Category'}
        return Response(content)