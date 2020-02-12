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
            path('courses/kanji/<int:id>/', views.kanji),
            path('courses/vocabulary/<int:id>/', views.vocabulary),
            path('kanji/<int:id>/', views.kanji),
            path('vocabulary/<int:id>/', views.vocabulary),
            path('texts/', views.texts),
            path('register/', views.UserRegister.as_view()),
            path('get-details/', views.GetDetails.as_view()),
            path('users/', views.ListAllUsers.as_view()),
            ])
        ),
    ])),
]

'''
        path('edit-account', views.EditAccount.as_view()), #POST only
        path('progress', views.ProgressController.as_view()),
        path('edit-text', views.EditText.as_view()), #POST only
'''