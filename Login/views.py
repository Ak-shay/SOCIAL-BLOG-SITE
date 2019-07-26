from django.shortcuts import render
from Blog.models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
	user = request.user
	followers = user.followers.all()
	following = user.follow.all()
	subscribers = user.subscribers.all()
	return render(request,'Login/profile.html',{'user': user, 'followers': followers,
												'subscribers': subscribers,
												'following': following})

@login_required
def any_profile(request, pk):
	any_user = CustomUser.objects.get(pk=pk)

	# form
	if request.POST.get('follow'):
		if any_user in request.user.follow.all():
			request.user.follow.remove(any_user)
		else:
			request.user.follow.add(any_user)

	if request.POST.get('sub'):
		if any_user in request.user.subscribe.all():
			request.user.subscribe.remove(any_user)
		else:
			request.user.subscribe.add(any_user)

	if any_user in request.user.follow.all():
		follow = True
	else:
		follow = False
	if any_user in request.user.subscribe.all():
		subscribe = True
	else:
		subscribe = False

	return render(request, 'Login/any_profile.html',{'any_user': any_user, 'follow': follow, 'subscribe': subscribe})

@login_required
def settings(request):
	return render(request, 'Login/settings.html',{})
