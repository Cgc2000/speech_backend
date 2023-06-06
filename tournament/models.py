from django.db import models

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

  class Meta:
      managed = True
      db_table = 'speech_tournaments'

