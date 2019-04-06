from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Like
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'Blog/post_list.html',{'posts':posts})

@login_required
def post_detail(request, pk):    #details of given post
    post = get_object_or_404(Post, pk=pk)

    #cliking the LIKE button
    if request.POST.get('like') == 'done':
        #user already liked the post
        if post.like_set.filter(author_like = request.user):
            l = post.like_set.get(author_like = request.user)
            l.delete()
            post.save()
        #user like the post
        else:
            l = Like()
            l.liked_post = post
            l.author_like = request.user
            l.publish()
            l.save()

    #cliking the DELETE button (only author of post can delete)
    #deletes the post and redirect to post list
    if request.POST.get('delete') == 'done':
        if (request.user == post.author_post):
            post.delete()
            return redirect('post_list')

    return render(request,'Blog/post_detail.html',{'post':post})

@login_required
def post_new(request):   #making new post for blog
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_post = request.user
            post.publish()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'Blog/post_new.html',{'form':form})

@login_required
def post_comment(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author_comment = request.user
            comment.publish()
            return redirect('post_detail',pk=pk)
    else:
        form = CommentForm()
    return render(request,'Blog/post_new.html',{'form':form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (request.user == post.author_post):   #only author post can edit his post
        if request.method == 'POST':
            form = PostForm(request.POST,instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author_post = request.user
                post.publish()
                return redirect('post_detail',pk=post.pk)
    form = PostForm()
    return render(request,'Blog/post_new.html',{'form':form})
