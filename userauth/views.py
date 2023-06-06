from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json


class UserRegister(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = custom_validation(request.data)
    serializer = UserRegisterSerializer(data=clean_data)
    if serializer.is_valid(raise_exception=True):
      user = serializer.create(clean_data)
      if user:
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
  permission_classes = (permissions.AllowAny,)
  authentication_classes = (SessionAuthentication,)
  ##
  def post(self, request):
    data = request.data
    assert validate_email(data)
    assert validate_password(data)
    serializer = UserLoginSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
      user = serializer.check_user(data)
      login(request, user)
      user_dict = {
        'firstName': user.getFirstName(),
        'lastName': user.getLastName(),
        'email': user.getEmail(),
        'id': user.getUserId()
      }
      response = json.dumps(user_dict)
      return Response(response, status=status.HTTP_200_OK)


class UserLogout(APIView):
  permission_classes = (permissions.AllowAny,)
  authentication_classes = ()
  def post(self, request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


class UserView(APIView):
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (SessionAuthentication,)
  ##
  def get(self, request):
    serializer = UserSerializer(request.user)
    return Response({'user': serializer.data}, status=status.HTTP_200_OK)

@csrf_exempt
def delete_users(request):
  try:
    AppUser.objects.using("speech-dev").delete()
  except Exception as e:
    print(e)
    return HttpResponse(2)
  count = AppUser.objects.using("speech-dev").count()
  if count == 0:
    return HttpResponse(0)
  return HttpResponse(1)
