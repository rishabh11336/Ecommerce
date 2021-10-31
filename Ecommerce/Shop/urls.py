from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.productpage, name='product'),
    path('category/<str:category>', views.category, name='category'),

]
