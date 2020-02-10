from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Course
# Create your views here.

def courses(request):
    data = list(Course.objects.values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)
