from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    user = request.user
    return render(request,'Login/profile.html',{'user':user})
