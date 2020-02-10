from django.urls import path, re_path, include
from django.contrib import admin
from django.http import JsonResponse

from . import views

urlpatterns = [
    path('api/v1/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include([
        path('v1/', include(
            [
            path('courses/', views.courses),
            path('kanji/<int:id>/', views.kanji),
            path('vocabulary/<int:id>/', views.vocabulary),
            path('texts/', views.texts),
            path('register/', views.UserRegister.as_view()),
            ])
        ),
    ])),
]
