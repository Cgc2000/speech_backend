from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
#from signup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('signup/', views.post_signup, name = "signup"),
    #path('deletesignup/', views.delete_signup, name = "deletesignup"),
    path('auth/', include('userauth.urls')),
    path('tournament/', include('tournament.urls')),
]