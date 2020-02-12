from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Course, Kanji, Vocabulary, Text, User, Progress
from .serializers import RegisterSerializer, EditUserSerializer, ProgressSerializer, TextSerializer
#registration
from rest_framework.views import APIView
from rest_framework import status, permissions, authentication
from oauth2_provider.settings import oauth2_settings
from braces.views import CsrfExemptMixin
from oauth2_provider.views.mixins import OAuthLibMixin
from django.db import transaction
import json
from django.utils.translation import gettext_lazy as _

#stuff
from django.utils.decorators import method_decorator
#from django.http import HttpResponse
#from django.views.generic import View
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.models import AccessToken
import re

#custom token view
from oauth2_provider.views.base import TokenView
from oauth2_provider.models import get_access_token_model, get_application_model
from oauth2_provider.signals import app_authorized

# Create your views here.

def courses(request):
    data = list(Course.objects.values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)

def kanji(request, id):
    data = list(Kanji.objects.filter(course=id).values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)
    
def kanji_all(request):
    data = list(Kanji.objects.values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)

def vocabulary(request, id):
    data = list(Vocabulary.objects.filter(course=id).values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)

def vocabulary_all(request):
    data = list(Vocabulary.objects.values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)

def texts(request):
    data = list(Text.objects.values())

    #allow returning non-dict data, an array in our case
    return JsonResponse(data, safe=False)


class CustomTokenView(TokenView):
    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_token_response(request)
        if status == 200:
            body = json.loads(body)
            access_token = body.get("access_token")
            if access_token is not None:
                token = get_access_token_model().objects.get(
                    token=access_token)
                app_authorized.send(
                    sender=self, request=request,
                    token=token)
                role = 'user'
                if token.user.is_staff == 1:
                    role = 'admin'
                body['role'] = role
                body = json.dumps(body)
        response = HttpResponse(content=body, status=status)
        for k, v in headers.items():
            response[k] = v
        return response

class UserRegister(OAuthLibMixin, APIView):
    #authentication_classes = [authentication.BasicAuthentication]
    
    permission_classes = (permissions.AllowAny,)

    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def post(self, request):
        if request.auth is None:
            data = request.data
            data = data.dict()
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        user = serializer.save()

                        url, headers, body, token_status = self.create_token_response(request)

                        if token_status != 200:
                            raise Exception(json.loads(body).get("error_description", body))

                        return JsonResponse(json.loads(body), safe=False, status=token_status)
                except Exception as e:
                    return JsonResponse(data={"error": (str(e))}, safe=False, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(data=serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse([], safe=False, status=status.HTTP_403_FORBIDDEN)

def getUser(request):
    app_tk = request.META["HTTP_AUTHORIZATION"]
    m = re.search('(Bearer)(\s)(.*)', app_tk)
    app_tk = m.group(3)
    acc_tk = AccessToken.objects.get(token=app_tk)
    user = acc_tk.user

    return user

class Template(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = getUser(request)
        return JsonResponse(user.id, safe=False)

    def post(self, request):
        user = getUser(request)

        return JsonResponse(user.id, safe=False)


class GetDetails(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = getUser(request)
        
        userLimited = dict()
        userLimited['id'] = user.id
        userLimited['name'] = user.username
        userLimited['email'] = user.email
        userLimited['sex'] = user.sex
        userLimited['surname'] = user.surname
        userLimited['surname'] = user.birthday
        if user.is_staff == 1:
            userLimited['role'] = 'admin'
        else:
            userLimited['role'] = 'user'
        
        userLimited['status'] = user.status

        odp = dict()
        odp['success'] = userLimited

        return JsonResponse(odp, safe=False)
    
    def post(self, request):
        user = getUser(request)
        
        userLimited = dict()
        userLimited['id'] = user.id
        userLimited['name'] = user.username
        userLimited['email'] = user.email
        userLimited['sex'] = user.sex
        userLimited['surname'] = user.surname
        userLimited['surname'] = user.birthday

        if user.is_staff == 1:
            userLimited['role'] = 'admin'
        else:
            userLimited['role'] = 'user'

        userLimited['status'] = user.status

        odp = dict()
        odp['success'] = userLimited

        return JsonResponse(odp, safe=False)

class ListAllUsers(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        data = list(User.objects.values())
        users = []
        for user in data:
            userLimited = dict()
            userLimited['id'] = user['id']
            userLimited['name'] = user['username']
            userLimited['email'] = user['email']
            userLimited['sex'] = user['sex']
            userLimited['surname'] = user['surname']
            userLimited['birthday'] = user['birthday']
            if user['is_staff'] == 1:
                userLimited['role'] = 'admin'
            else:
                userLimited['role'] = 'user'
            userLimited['status'] = user['status']

            #users = DB::table('users')->select('id', 'name', 'email', 'created_at', 'updated_at', 'sex', 'surname', 'birthday', 'role', 'status')->get();
            users.append(userLimited)

        resp = dict()
        resp['success'] = users
        #allow returning non-dict data, an array in our case
        return JsonResponse(resp, safe=False)


class EditAccount(APIView): #OAuthLibMixin
    permission_classes = (permissions.IsAuthenticated,)

    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def post(self, request):
        user = getUser(request)
        data = request.data
        data = data.dict()
        serializer = EditUserSerializer(data=data)
        
        try:
            if serializer.is_valid(True):
                try:
                    user = serializer.update(user, serializer.validated_data)

                    resp = dict()
                    resp['success'] = 'success'
                    return JsonResponse(resp, safe=False)
                except Exception as e:
                    return JsonResponse(data={"error": (str(e))}, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)

class ProgressController(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = getUser(request)

        data = list(Progress.objects.filter(user_id=user.id).values())
        return JsonResponse(data, safe=False)

    def post(self, request):
        user = getUser(request)
        data = request.data
        data = data.dict()
        data['user'] = str(user.id)
        serializer = ProgressSerializer(data=data)
        
        try:
            if serializer.is_valid(True):
                try:
                    #instance = Progress.objects.filter(user_id=user.id, category_id=data['category'])
                    instance = Progress.objects.filter(user_id=user.id, game=data['game'], category_id=data['category']).first()

                    if(instance):
                        progress = serializer.update(instance, serializer.validated_data)
                    else: 
                        progress = serializer.save() #user, serializer.validated_data)

                    resp = dict()
                    resp['success'] = 'success'
                    return JsonResponse(resp, safe=False)
                except Exception as e:
                    return JsonResponse(data={"error": (str(e))}, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)
class EditText(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request):
        data = request.data
        data = data.dict()
        serializer = TextSerializer(data=data)
        
        try:
            if serializer.is_valid(True):
                try:
                    instance = Text.objects.filter(id=data['id']).first()
                    if(instance):
                        text = serializer.update(instance, serializer.validated_data)
                    else:
                        return JsonResponse("No such id", safe=False)
                    
                    resp = dict()
                    resp['success'] = 'success'
                    return JsonResponse(resp, safe=False)
                except Exception as e:
                    return JsonResponse(data={"error": (str(e))}, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)
