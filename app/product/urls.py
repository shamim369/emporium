from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('category/', views.CategoryView.as_view(), name='category_view'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category_detail_view'),
]

# http://127.0.0.1:8000/api/product/category/
# http://127.0.0.1:8000/api/product/category/1/