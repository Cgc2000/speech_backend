from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import TournamentRegister, CompetitorSignup, Entries, Judges
UserModel = get_user_model()

def custom_validation(data):
    registerUserId = data['registerUserId']
    tournamentName = data['tournamentName'].strip()
    tournamentLevel = data['tournamentLevel'].strip()
    hostSchool = data['hostSchool'].strip()
    managerName = data['managerName'].strip()
    managerEmail = data['managerEmail'].strip()
    managerPhone = data['managerPhone'].strip()
    tournamentCity = data['tournamentCity'].strip()
    tournamentState = data['tournamentState'].strip()
    events = data['events']

    if not registerUserId or not UserModel.objects.using('speech-dev').filter(speechCoachUsersId=registerUserId).exists():
        raise ValidationError('User account error: Please make sure you are logged in')

    if not tournamentName:
        raise ValidationError('A tournament name is needed.')
    
    if not hostSchool:
        raise ValidationError('A host school is needed.')

    if not managerName:
        raise ValidationError('A manager name is needed.')

    if not managerEmail:
        raise ValidationError('A manager email is needed.')

    if not managerPhone:
        raise ValidationError('A manager phone is needed.')

    if not tournamentCity:
        raise ValidationError('A valid location is needed.')
    if not events or len(events) == 0:
        raise ValidationError('You must have at least one event.')
    return data


def user_validation(data):
    userId = data['userId']
    if not userId or not UserModel.objects.using('speech-dev').filter(speechCoachUsersId=userId).exists():
        raise ValidationError('Please log in.')
    return data

def tournament_validation(data):
    tournamentId = data['tournamentId']
    if not tournamentId or not TournamentRegister.objects.using('speech-dev').filter(tournamentId=tournamentId).exists():
        raise ValidationError('Tournament does not exist.')
    return data

def competitor_validation(data):
    registerUserId = data['registerUserId']
    if not registerUserId or not UserModel.objects.using('speech-dev').filter(speechCoachUsersId=registerUserId).exists():
        raise ValidationError('Please log in.')
    tournamentId = data['tournamentId']
    if not tournamentId or not TournamentRegister.objects.using('speech-dev').filter(tournamentId=tournamentId).exists():
        raise ValidationError('Tournament does not exist.')
    competitorSchool = data['competitorSchool']
    if not competitorSchool:
        raise ValidationError('Please enter a school name.')
    coachName = data['coachName']
    if not coachName:
        raise ValidationError('Please enter a coach name.')
    coachEmail = data['coachEmail']
    if not coachEmail:
        raise ValidationError('Please enter a coach email.')
    coachPhone = data['coachPhone']
    if not coachPhone:
        raise ValidationError('Please enter a coach phone.')
    return data

def entry_validation(data):
    tournamentId = data['tournamentId']
    if not tournamentId or not TournamentRegister.objects.using('speech-dev').filter(tournamentId=tournamentId).exists():
        raise ValidationError('Tournament does not exist.')
    competitorId = data['competitorId']
    if not competitorId or not CompetitorSignup.objects.using('speech-dev').filter(competitorId=competitorId).exists():
        raise ValidationError('Competitor school does not exist.')
    schoolKey = data['schoolKey']
    if not schoolKey:
        raise ValidationError('Error finding competitor school; please ensure you are logged in and try again.')
    name = data['name']
    if not name:
        raise ValidationError('Please enter a student name.')
    event = data['event']
    if not event:
        raise ValidationError('Please select an event.')
    return data

def delete_entry_validation(data):
    competitorId = data['competitorId']
    if not competitorId or not CompetitorSignup.objects.using('speech-dev').filter(competitorId=competitorId).exists():
        raise ValidationError('Tournament does not exist.')
    entryId = data['entryId']
    if not entryId or not Entries.objects.using('speech-dev').filter(entryId=entryId).exists():
        raise ValidationError('Tournament does not exist.')
    return data

def judge_validation(data):
    tournamentId = data['tournamentId']
    if not tournamentId or not TournamentRegister.objects.using('speech-dev').filter(tournamentId=tournamentId).exists():
        raise ValidationError('Tournament does not exist.')
    competitorId = data['competitorId']
    if not competitorId or not CompetitorSignup.objects.using('speech-dev').filter(competitorId=competitorId).exists():
        raise ValidationError('Competitor school does not exist.')
    schoolKey = data['schoolKey']
    if not schoolKey:
        raise ValidationError('Error finding competitor school; please ensure you are logged in and try again.')
    name = data['name']
    if not name:
        raise ValidationError('Please enter a judge name.')
    email = data['email']
    if not email:
        raise ValidationError('Please enter an judge email.')
    return data

def delete_judge_validation(data):
    competitorId = data['competitorId']
    if not competitorId or not CompetitorSignup.objects.using('speech-dev').filter(competitorId=competitorId).exists():
        raise ValidationError('Tournament does not exist.')
    judgeId = data['judgeId']
    if not judgeId or not Judges.objects.using('speech-dev').filter(judgeId=judgeId).exists():
        raise ValidationError('Tournament does not exist.')
    return data