from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
  def create_user(self, firstName, lastName, email, password):
    if not firstName:
      raise ValueError('First name is required.')
    if not lastName:
      raise ValueError('Last name is required.')
    if not email:
      raise ValueError('An email is required.')
    if not password:
      raise ValueError('A password is required.')
    email = self.normalize_email(email)
    start_id = -1
    try:
      start_id = int(AppUser.objects.using("speech-dev").latest('speechCoachUsersId').speechCoachUsersId)
    except Exception:
      total_row_count = AppUser.objects.using("speech-dev").count()
      if total_row_count == 0:
        start_id = 0
    user = self.model(speechCoachUsersId=(start_id + 1), email=email, firstName=firstName, lastName=lastName)
    user.set_password(password)
    user.save(using='speech-dev')
    return user


class AppUser(AbstractBaseUser, PermissionsMixin):
  speechCoachUsersId = models.IntegerField(primary_key=True)
  firstName = models.TextField()
  lastName = models.TextField()
  email = models.TextField(unique=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['firstName', 'lastName']
  objects = AppUserManager()
  def __str__(self):
    return self.firstName + " " + self.lastName
  def getFirstName(self):
    return self.firstName
  def getLastName(self):
    return self.lastName
  def getEmail(self):
    return self.email
  def getPassword(self):
    return self.password
  def getUserId(self):
    return self.speechCoachUsersId

  class Meta:
      managed = True
      db_table = 'speech_coach_users'