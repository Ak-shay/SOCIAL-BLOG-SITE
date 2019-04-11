from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    user = request.user
    return render(request,'Login/profile.html',{'user':user})

@login_required
def any_profile(request, pk):
    any_user = User.objects.get(pk=pk)
    return render(request, 'Login/any_profile.html',{'any_user':any_user})
