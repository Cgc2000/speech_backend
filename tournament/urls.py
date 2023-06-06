from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.TournamentRegisterView.as_view(), name='register'),
	path('get_user_tournaments/', views.GetUserTournamentsView.as_view(), name='get_user_tournaments')
]