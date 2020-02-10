from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Course, Kanji
# Create your views here.

def courses(request):
    data = list(Course.objects.values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)
    
def kanji(request, id):
    data = list(Kanji.objects.filter(course=id).values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)
