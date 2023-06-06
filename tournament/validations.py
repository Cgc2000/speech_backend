from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
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
    return data


def user_validation(data):
    userId = data['userId']
    if not userId or not UserModel.objects.using('speech-dev').filter(speechCoachUsersId=userId).exists():
        raise ValidationError('please log in')
    return data

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True