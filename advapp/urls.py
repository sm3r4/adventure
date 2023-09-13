
from django.urls import path 
from . import views

urlpatterns = [
   
    path('adventure',views.index,name='index'),
    path('details/<int:pk>',views.details,name='details'),
]