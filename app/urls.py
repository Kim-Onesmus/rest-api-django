from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_list, name='drinks'),
    path('drink_details/<int:id>/', views.drink_details, name='drink_details')
]