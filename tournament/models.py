from django.db import models
from django.contrib.postgres.fields import ArrayField

class TournamentRegister(models.Model):
  tournamentId = models.IntegerField(primary_key=True)
  registerUserId = models.IntegerField()
  tournamentName = models.TextField()
  tournamentLevel = models.TextField()
  hostSchool = models.TextField()
  managerName = models.TextField()
  managerEmail = models.TextField()
  managerPhone = models.TextField()
  tournamentCity = models.TextField()
  tournamentState = models.TextField()
  accessCode = models.TextField()
  schoolsEntered = models.IntegerField()
  events = ArrayField(
    models.TextField()
  )
  def getTournamentId(self):
    return self.tournamentId
  def getRegisterUserId(self):
    return self.registerUserId
  def getTournamentName(self):
    return self.tournamentName
  def getTournamentLevel(self):
    return self.tournamentLevel
  def getHostSchool(self):
    return self.hostSchool
  def getManagerName(self):
    return self.managerName
  def getManagerEmail(self):
    return self.managerEmail
  def getManagerPhone(self):
    return self.managerPhone
  def getTournamentCity(self):
    return self.tournamentCity
  def getTournamentState(self):
    return self.tournamentState
  def getAccessCode(self):
    return self.accessCode
  def getSchoolsEntered(self):
    return self.schoolsEntered
  def getEvents(self):
    return self.events

  class Meta:
      managed = True
      db_table = 'speech_tournaments'

class CompetitorSignup(models.Model):
  competitorId = models.IntegerField(primary_key=True)
  schoolKey = models.CharField(max_length=1)
  tournamentId = models.IntegerField()
  registerUserId = models.IntegerField()
  competitorSchool = models.TextField()
  coachName = models.TextField()
  coachEmail = models.TextField()
  coachPhone = models.TextField()
  def getCompetitorId(self):
    return self.competitorId
  def getSchoolKey(self):
    return self.schoolKey
  def getTournamentId(self):
    return self.tournamentId
  def getRegisterUserId(self):
    return self.registerUserId
  def getCompetitorSchool(self):
    return self.competitorSchool
  def getCoachName(self):
    return self.coachName
  def getCoachEmail(self):
    return self.coachEmail
  def getCoachPhone(self):
    return self.coachPhone

  class Meta:
      managed = True
      db_table = 'speech_competitors'

class Entries(models.Model):
  entryId = models.IntegerField(primary_key=True)
  studentId = models.IntegerField()
  competitorId = models.IntegerField()
  schoolKey = models.CharField(max_length=1)
  tournamentId = models.IntegerField()
  name = models.TextField()
  event = models.TextField()
  def getEntryId(self):
    return self.entryId
  def getStudentId(self):
    return self.studentId
  def getCompetitorId(self):
    return self.competitorId
  def getSchoolKey(self):
    return self.schoolKey
  def getTournamentId(self):
    return self.tournamentId
  def getName(self):
    return self.name
  def getEvent(self):
    return self.event

  class Meta:
      managed = True
      db_table = 'speech_entries'
