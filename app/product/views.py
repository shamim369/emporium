from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category

# Create your views here.
class CategoryView(APIView):

    def get(self, request):
        category_list = Category.objects.all()
        print("------------------------------------\n", category_list)

        a = [x.category_title for x in category_list]
        content = {'message': a}
        return Response(content)
