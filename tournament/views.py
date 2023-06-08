from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TournamentRegisterSerializer, CompetitorSignupSerializer
from rest_framework import permissions, status
from .validations import custom_validation, user_validation, tournament_validation, competitor_validation
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from .models import TournamentRegister, CompetitorSignup


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

class CompetitorSignupView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = competitor_validation(request.data)
    serializer = CompetitorSignupSerializer(data=clean_data)
    if serializer.is_valid(raise_exception=True):
      competitor = serializer.create(clean_data)
      if competitor:
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
        'tournamentState': i.getTournamentState(),
        'accessCode': i.getAccessCode(),
        'schoolsEntered': i.getSchoolsEntered()
      })
      response = json.dumps(tournament_dicts)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetUserEnteredView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = user_validation(request.data)
    entries = CompetitorSignup.objects.using("speech-dev").filter(registerUserId=clean_data['userId'])
    if entries:
      tournament_dicts = []
      for i in entries:
        tournamentId = i.getTournamentId()
        tournament = TournamentRegister.objects.using("speech-dev").get(tournamentId=tournamentId)
        tournament_dicts.append({
        'tournamentId': tournament.getTournamentId(),
        'registerUserId': tournament.getRegisterUserId(),
        'tournamentName': tournament.getTournamentName(),
        'tournamentLevel': tournament.getTournamentLevel(),
        'hostSchool': tournament.getHostSchool(),
        'managerName': tournament.getManagerName(),
        'managerEmail': tournament.getManagerEmail(),
        'managerPhone': tournament.getManagerPhone(),
        'tournamentCity': tournament.getTournamentCity(),
        'tournamentState': tournament.getTournamentState(),
        'accessCode': tournament.getAccessCode(),
        'schoolsEntered': tournament.getSchoolsEntered()
      })
      response = json.dumps(tournament_dicts)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetAllTournamentsView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    tournaments = TournamentRegister.objects.using("speech-dev").all()
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
        'tournamentState': i.getTournamentState(),
        'accessCode': i.getAccessCode(),
        'schoolsEntered': i.getSchoolsEntered()
      })
      response = json.dumps(tournament_dicts)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetTournamentByCodeView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    tournament = TournamentRegister.objects.using("speech-dev").get(accessCode=request.data['accessCode'])
    if tournament:
      tournament_dict = {
        'tournamentId': tournament.getTournamentId(),
        'registerUserId': tournament.getRegisterUserId(),
        'tournamentName': tournament.getTournamentName(),
        'tournamentLevel': tournament.getTournamentLevel(),
        'hostSchool': tournament.getHostSchool(),
        'managerName': tournament.getManagerName(),
        'managerEmail': tournament.getManagerEmail(),
        'managerPhone': tournament.getManagerPhone(),
        'tournamentCity': tournament.getTournamentCity(),
        'tournamentState': tournament.getTournamentState(),
        'accessCode': tournament.getAccessCode(),
        'schoolsEntered': tournament.getSchoolsEntered()
      }
      response = json.dumps(tournament_dict)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetTournamentByIdView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    print(request.data)
    tournamentId = request.data['tournamentId']
    print(tournamentId)
    tournament = TournamentRegister.objects.using("speech-dev").get(tournamentId=tournamentId)
    if tournament:
      tournament_dict = {
        'tournamentId': tournament.getTournamentId(),
        'registerUserId': tournament.getRegisterUserId(),
        'tournamentName': tournament.getTournamentName(),
        'tournamentLevel': tournament.getTournamentLevel(),
        'hostSchool': tournament.getHostSchool(),
        'managerName': tournament.getManagerName(),
        'managerEmail': tournament.getManagerEmail(),
        'managerPhone': tournament.getManagerPhone(),
        'tournamentCity': tournament.getTournamentCity(),
        'tournamentState': tournament.getTournamentState(),
        'accessCode': tournament.getAccessCode(),
        'schoolsEntered': tournament.getSchoolsEntered()
      }
      response = json.dumps(tournament_dict)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteTournamentView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = tournament_validation(request.data)
    try:
      TournamentRegister.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId']).delete()
      CompetitorSignup.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId']).delete()
      return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
      print(e)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteCompetitorView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = tournament_validation(request.data)
    try:
      tournament = TournamentRegister.objects.using("speech-dev").get(tournamentId=clean_data['tournamentId'])
      tournament.schoolsEntered -= 1
      tournament.save(using="speech-dev")
      CompetitorSignup.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId'], registerUserId=clean_data['registerUserId']).delete()
      return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
      print(e)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)