from django.urls import path, include
from . import views

urlpatterns = [
	path('accounts/', include('allauth.urls')),
	path('accounts/settings/',views.settings, name='settings'),
    path('accounts/profile/', views.user_profile, name = 'profile'),
	path('profile/<int:pk>', views.any_profile, name= 'any_profile'),
]
