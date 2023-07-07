from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TournamentRegisterSerializer, CompetitorSignupSerializer, EntriesSerializer, JudgesSerializer
from rest_framework import permissions, status
from .validations import custom_validation, user_validation, tournament_validation, competitor_validation, entry_validation, delete_entry_validation, judge_validation, delete_judge_validation
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from .models import TournamentRegister, CompetitorSignup, Entries, Judges


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

class EntriesView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = entry_validation(request.data)
    serializer = EntriesSerializer(data=clean_data)
    if serializer.is_valid(raise_exception=True):
      entry = serializer.create(clean_data)
      if entry:
        entry_dict = {
          'entryId': entry.getEntryId(),
          'studentId': entry.getStudentId(),
          'competitorId': entry.getCompetitorId(),
          'schoolKey': entry.getSchoolKey(),
          'tournamentId': entry.getTournamentId(),
          'name': entry.getName(),
          'event': entry.getEvent(),
          'additionalNames': entry.getAdditionalNames()
        }
        response = json.dumps(entry_dict)
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class JudgesView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = judge_validation(request.data)
    serializer = JudgesSerializer(data=clean_data)
    if serializer.is_valid(raise_exception=True):
      judge = serializer.create(clean_data)
      print("nice!")
      if judge:
        judge_dict = {
          'judgeId': judge.getJudgeId(),
          'judgeCode': judge.getJudgeCode(),
          'competitorId': judge.getCompetitorId(),
          'schoolKey': judge.getSchoolKey(),
          'tournamentId': judge.getTournamentId(),
          'name': judge.getName(),
          'email': judge.getEmail(),
          'isActivated': judge.getIsActivated()
        }
        response = json.dumps(judge_dict)
        return Response(response, status=status.HTTP_201_CREATED)
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
        'schoolsEntered': i.getSchoolsEntered(),
        'events': i.getEvents(),
        'rooms': i.getRooms()
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
        'competitorSchool': i.getCompetitorSchool(),
        'competitorId': i.getCompetitorId(),
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
        'schoolsEntered': tournament.getSchoolsEntered(),
        'events': tournament.getEvents(),
        'rooms': tournament.getRooms()
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
        'schoolsEntered': i.getSchoolsEntered(),
        'events': i.getEvents(),
        'rooms': i.getRooms()
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
        'schoolsEntered': tournament.getSchoolsEntered(),
        'events': tournament.getEvents(),
        'rooms': tournament.getRooms()
      }
      response = json.dumps(tournament_dict)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetTournamentByIdView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    tournamentId = request.data['tournamentId']
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
        'schoolsEntered': tournament.getSchoolsEntered(),
        'events': tournament.getEvents(),
        'rooms': tournament.getRooms()
      }
      response = json.dumps(tournament_dict)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetCompetitorsView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    tournamentId = request.data['tournamentId']
    competitors = CompetitorSignup.objects.using("speech-dev").filter(tournamentId=tournamentId)
    if competitors:
      competitors_dicts = []
      for i in competitors:
        competitor_dict = {
          'competitorId': i.getCompetitorId(),
          'schoolKey': i.getSchoolKey(),
          'tournamentId': i.getTournamentId(),
          'registerUserId': i.getRegisterUserId(),
          'competitorSchool': i.getCompetitorSchool(),
          'coachName': i.getCoachName(),
          'coachEmail': i.getCoachEmail(),
          'coachPhone': i.getCoachPhone(),
          'numEntries': i.getNumEntries()
        }
        competitors_dicts.append(competitor_dict)
      response = json.dumps(competitors_dicts)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetCompetitorByIdView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    competitorId = request.data['competitorId']
    competitor = CompetitorSignup.objects.using("speech-dev").get(competitorId=competitorId)
    if competitor:
      competitor_dict = {
        'competitorId': competitor.getCompetitorId(),
        'schoolKey': competitor.getSchoolKey(),
        'tournamentId': competitor.getTournamentId(),
        'registerUserId': competitor.getRegisterUserId(),
        'competitorSchool': competitor.getCompetitorSchool(),
        'coachName': competitor.getCoachName(),
        'coachEmail': competitor.getCoachEmail(),
        'coachPhone': competitor.getCoachPhone()
      }
      response = json.dumps(competitor_dict)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetEntriesView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    competitorId = request.data['competitorId']
    entries = Entries.objects.using("speech-dev").filter(competitorId=competitorId)
    if entries:
      entries_dict = []
      for i in entries:
        entry_dict = {
          'entryId': i.getEntryId(),
          'studentId': i.getStudentId(),
          'competitorId': i.getCompetitorId(),
          'schoolKey': i.getSchoolKey(),
          'tournamentId': i.getTournamentId(),
          'name': i.getName(),
          'event': i.getEvent(),
          'additionalNames': i.getAdditionalNames()
        }
        entries_dict.append(entry_dict)
      response = json.dumps(entries_dict)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetJudgesView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    competitorId = request.data['competitorId']
    judges = Judges.objects.using("speech-dev").filter(competitorId=competitorId)
    if judges:
      judges_dict = []
      for i in judges:
        judge_dict = {
          'judgeId': i.getJudgeId(),
          'judgeCode': i.getJudgeCode(),
          'competitorId': i.getCompetitorId(),
          'schoolKey': i.getSchoolKey(),
          'tournamentId': i.getTournamentId(),
          'name': i.getName(),
          'email': i.getEmail(),
          'isActivated': i.getIsActivated()
        }
        judges_dict.append(judge_dict)
      response = json.dumps(judges_dict)
      return Response(response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteTournamentView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = tournament_validation(request.data)
    try:
      TournamentRegister.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId']).delete()
      CompetitorSignup.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId']).delete()
      Entries.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId']).delete()
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
      CompetitorSignup.objects.using("speech-dev").filter(competitorId=clean_data['competitorId']).delete()
      Entries.objects.using("speech-dev").filter(competitorId=clean_data['competitorId']).delete()
      return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
      print(e)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteEntryView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = delete_entry_validation(request.data)
    try:
      Entries.objects.using("speech-dev").filter(entryId=clean_data['entryId']).delete()
      entries_count = Entries.objects.using("speech-dev").filter(competitorId=clean_data['competitorId']).count()
      competitor = CompetitorSignup.objects.using("speech-dev").get(competitorId=clean_data['competitorId'])
      competitor.numEntries = entries_count
      competitor.save(using="speech-dev")
      return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
      print(e)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteJudgeView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = delete_judge_validation(request.data)
    try:
      Judges.objects.using("speech-dev").filter(judgeId=clean_data['judgeId']).delete()
      judges_count = Judges.objects.using("speech-dev").filter(competitorId=clean_data['competitorId']).count()
      competitor = CompetitorSignup.objects.using("speech-dev").get(competitorId=clean_data['competitorId'])
      competitor.numJudges = judges_count
      competitor.save(using="speech-dev")
      return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
      print(e)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetTournamentEntriesView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = tournament_validation(request.data)
    try:
      entries = Entries.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId'])
      if entries:
        entries_dict = []
        for i in entries:
          entry_dict = {
            'entryId': i.getEntryId(),
            'studentId': i.getStudentId(),
            'competitorId': i.getCompetitorId(),
            'schoolKey': i.getSchoolKey(),
            'tournamentId': i.getTournamentId(),
            'name': i.getName(),
            'event': i.getEvent(),
            'additionalNames': i.getAdditionalNames()
          }
          entries_dict.append(entry_dict)
        response = json.dumps(entries_dict)
        return Response(response, status=status.HTTP_201_CREATED)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      print(e)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class GetEventsView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request):
    clean_data = tournament_validation(request.data)
    try:
      try:
        entries = Entries.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId'])
      except Exception as e:
        print(e)
        entries = []
      events_dict = []
      for event in clean_data['events']:
        event_dict = []
        for i in entries:
          if i.getEvent() == event:
            entry_dict = {
              'entryId': i.getEntryId(),
              'studentId': i.getStudentId(),
              'competitorId': i.getCompetitorId(),
              'schoolKey': i.getSchoolKey(),
              'tournamentId': i.getTournamentId(),
              'name': i.getName(),
              'event': i.getEvent(),
              'additionalNames': i.getAdditionalNames()
            }
            event_dict.append(entry_dict)
        events_dict.append([event, event_dict])
      response = json.dumps(events_dict)
      return Response(response, status=status.HTTP_201_CREATED)
    except Exception as e:
      print(e)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)