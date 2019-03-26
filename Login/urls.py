from django.urls import path, include
from . import views

urlpatterns = [
	path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.user_profile, name = 'profile'),
]
