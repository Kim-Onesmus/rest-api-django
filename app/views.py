from django.shortcuts import render
from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinkSerializer


def drink_list(request):
    drinks = Drinks.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({'drinks':serializer.data}, safe=False)