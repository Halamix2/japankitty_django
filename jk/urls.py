from django.urls import path, re_path, include
from django.contrib import admin
from django.http import JsonResponse

from . import views

urlpatterns = [
    
    path('api/', include([
        path('v1/', include(
            [
            path('token/', views.CustomTokenView.as_view()),
            path('courses/', views.courses),
            path('courses/kanji/', views.courses_kanji),
            path('courses/vocabulary/', views.courses_vocabulary),
            path('kanji/<int:id>/', views.kanji),
            path('vocabulary/<int:id>/', views.vocabulary),
            path('kanji/', views.kanji_all),
            path('vocabulary/', views.vocabulary_all),
            path('texts/', views.texts),
            path('register/', views.UserRegister.as_view()),
            path('get-details/', views.GetDetails.as_view()),
            path('users/', views.ListAllUsers.as_view()),
            path('edit-account/', views.EditAccount.as_view()),
            path('progress/', views.ProgressController.as_view()),
            path('edit-text/', views.EditText.as_view()),
            ])
        ),
    ])),
    path('api/v1/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
