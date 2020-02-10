from django.urls import path, re_path, include
from django.contrib import admin
from django.http import JsonResponse

from . import views

urlpatterns = [
    path('api/', include([
        path('v1/', include(
            [
            path('courses/', views.courses),
            path('kanji/<int:id>/', views.kanji),
            ])
        ),
    ])),
]
