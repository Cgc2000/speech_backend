from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import TournamentRegister, CompetitorSignup
import random
import string

class TournamentRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = TournamentRegister
		fields = ('registerUserId', 'tournamentName', 'tournamentLevel', 'hostSchool', 'managerName', 'managerEmail', 'managerPhone', 'tournamentCity', 'tournamentState')
	def create(self, clean_data):
		start_id = -1
		try:
			start_id = int(TournamentRegister.objects.using("speech-dev").latest('tournamentId').tournamentId)
		except Exception:
			total_row_count = TournamentRegister.objects.using("speech-dev").count()
			if total_row_count == 0:
				start_id = 0
		code = ''
		code_valid = False
		while not code_valid:
			code = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]).upper()
			if not TournamentRegister.objects.using('speech-dev').filter(accessCode=code).exists():
				code_valid = True
		tournament = TournamentRegister(tournamentId=(start_id + 1), registerUserId=clean_data['registerUserId'], tournamentName=clean_data['tournamentName'], tournamentLevel=clean_data['tournamentLevel'], hostSchool=clean_data['hostSchool'], managerName=clean_data['managerName'], managerEmail=clean_data['managerEmail'], managerPhone=clean_data['managerPhone'], tournamentCity=clean_data['tournamentCity'], tournamentState=clean_data['tournamentState'], accessCode=code, schoolsEntered=0)
		tournament.save(using='speech-dev')
		return tournament

class CompetitorSignupSerializer(serializers.ModelSerializer):
	class Meta:
		model = CompetitorSignup
		fields = ('registerUserId', 'tournamentId', 'competitorSchool', 'coachName', 'coachEmail', 'coachPhone')
	def create(self, clean_data):
		start_id = 0
		try:
			start_id = CompetitorSignup.objects.using("speech-dev").latest('competitorId').competitorId
		except Exception:
			total_row_count = CompetitorSignup.objects.using("speech-dev").count()
			if total_row_count == 0:
				start_id = 0
		start_key = 'A'
		def next_alpha(s):
			return chr((ord(s.upper())+1))
		try:
			old_key = CompetitorSignup.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId']).latest('schoolKey').schoolKey
			start_key = next_alpha(start_key)
		except Exception:
			total_row_count = CompetitorSignup.objects.using("speech-dev").filter(tournamentId=clean_data['tournamentId']).count()
			if total_row_count == 0:
				start_key = 'A'
		print(start_key)
		competitor = CompetitorSignup(competitorId=(start_id + 1), schoolKey = start_key, registerUserId=clean_data['registerUserId'], tournamentId=clean_data['tournamentId'], competitorSchool=clean_data['competitorSchool'], coachName=clean_data['coachName'], coachEmail=clean_data['coachEmail'], coachPhone=clean_data['coachPhone'])
		competitor.save(using='speech-dev')
		tournament = TournamentRegister.objects.using("speech-dev").get(tournamentId=clean_data['tournamentId'])
		tournament.schoolsEntered += 1
		tournament.save(using="speech-dev")
		return competitor