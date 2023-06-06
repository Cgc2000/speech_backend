from rest_framework import serializers
from django.core.exceptions import ValidationError
from .authenticate import authenticate
from .models import TournamentRegister

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
		tournament = TournamentRegister(tournamentId=(start_id + 1), registerUserId=clean_data['registerUserId'], tournamentName=clean_data['tournamentName'], tournamentLevel=clean_data['tournamentLevel'], hostSchool=clean_data['hostSchool'], managerName=clean_data['managerName'], managerEmail=clean_data['managerEmail'], managerPhone=clean_data['managerPhone'], tournamentCity=clean_data['tournamentCity'], tournamentState=clean_data['tournamentState'])
		tournament.save(using='speech-dev')
		return tournament