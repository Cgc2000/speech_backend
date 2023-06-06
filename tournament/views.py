from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TournamentRegisterSerializer
from rest_framework import permissions, status
from .validations import custom_validation, user_validation
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from .models import TournamentRegister


class TournamentRegisterView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = custom_validation(request.data)
    serializer = TournamentRegisterSerializer(data=clean_data)
    if serializer.is_valid(raise_exception=True):
      tournament = serializer.create(clean_data)
      if tournament:
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetUserTournamentsView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = user_validation(request.data)
    tournaments = TournamentRegister.objects.using("speech-dev").filter(registerUserId=clean_data['userId'])
    if tournaments:
      tournament_dicts = []
      for i in tournaments:
        tournament_dicts.append({
        'tournamentId': i.getTournamentId(),
        'registerUserId': i.getRegisterUserId(),
        'tournamentName': i.getTournamentName(),
        'tournamentLevel': i.getTournamentLevel(),
        'hostSchool': i.getHostSchool(),
        'managerName': i.getManagerName(),
        'managerEmail': i.getManagerEmail(),
        'managerPhone': i.getManagerPhone(),
        'tournamentCity': i.getTournamentCity(),
        'tournamentState': i.getTournamentState()
      })
      response = json.dumps(tournament_dicts)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
