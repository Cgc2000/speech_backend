from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.TournamentRegisterView.as_view(), name='register'),
	path('get_user_tournaments/', views.GetUserTournamentsView.as_view(), name='get_user_tournaments'),
	path('get_all_tournaments/', views.GetAllTournamentsView.as_view(), name='get_all_tournaments'),
	path('delete_tournament/', views.DeleteTournamentView.as_view(), name='delete_tournament'),
	path('get_tournament_by_code/', views.GetTournamentByCodeView.as_view(), name='get_tournament_by_code'),
	path('get_by_id/', views.GetTournamentByIdView.as_view(), name='get_by_id'),
	path('signup/', views.CompetitorSignupView.as_view(), name='signup'),
	path('get_user_entered/', views.GetUserEnteredView.as_view(), name='get_user_entered'),
	path('delete_competitor/', views.DeleteCompetitorView.as_view(), name='delete_competitor'),
	path('get_competitors/', views.GetCompetitorsView.as_view(), name='get_competitors'),
	path('get_competitor_by_id/', views.GetCompetitorByIdView.as_view(), name='get_competitor_by_id'),
	path('post_entry/', views.EntriesView.as_view(), name='post_entry'),
	path('get_entries/', views.GetEntriesView.as_view(), name='get_entries'),
	path('delete_entry/', views.DeleteEntryView.as_view(), name='delete_entry'),
	path('get_tournament_entries/', views.GetTournamentEntriesView.as_view(), name='get_tournament_entries'),
	path('get_events/', views.GetEventsView.as_view(), name='get_events'),
	path('post_judge/', views.JudgesView.as_view(), name='post_judge'),
	path('get_judges/', views.GetJudgesView.as_view(), name='get_judges'),
	path('delete_judge/', views.DeleteJudgeView.as_view(), name='delete_judge')
]