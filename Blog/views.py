from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.utils import timezone
from django.urls import reverse

from .forms import PostForm, CommentForm
from .models import Post, Like, Comment, CommentLike


class PostListView(ListView):
    """Returns all the post published till now."""
    context_object_name = 'posts'
    template_name = 'Blog/post_list.html'

    def get_queryset(self):
        if 'search' in self.request.GET:
            searched_value = self.request.GET.get('search')
            posts = Post.objects.filter(title__icontains = searched_value,
                                        published_date__lte=timezone.now())
        else:
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

        return posts


class SelfPostListView(LoginRequiredMixin, ListView):
    """Returns posts made by the user. """
    context_object_name = 'posts'
    template_name = 'Blog/post_list.html'

    def get_queryset(self):
        if 'search' in self.request.GET:
            searched_value = self.request.GET.get('search')
            posts = Post.objects.filter(title__icontains = searched_value,
                                        published_date__lte=timezone.now(),
                                        author_post=self.request.user.pk)
        else:
            posts = Post.objects.filter(published_date__lte=timezone.now(),
                                        author_post=self.request.user.pk).order_by('-published_date')
       
        return posts


class PostView(LoginRequiredMixin, View):
    """returns details of a post"""
    context_object_name = 'post'
    template_name = 'Blog/post_detail.html'

    def get_object(self):
        if self.kwargs['pk']:
            obj = get_object_or_404(Post, pk=self.kwargs['pk'])
            return obj

    def get(self, *args, **kwargs):
        context = {}
        post = self.get_object()
        context[self.context_object_name] = post
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        post = self.get_object()
        comments = post.comment_set.all()

        # When Like button is clicked
        if self.request.POST.get('like') == 'done':
            # If user already liked, delete this like
            if post.like_set.filter(author_like=self.request.user):
                l = post.like_set.get(author_like=self.request.user)
                l.delete()
            # otherwise like this post
            else:
                l = Like.objects.create(author_like=self.request.user, liked_post=post, published_date=timezone.now())

        #When Delete button is clicked
        if self.request.POST.get('delete') == 'done':
            #only author of post delete post.
            if (self.request.user == post.author_post):
                post.delete()
                return redirect('post_list')

        #comments view        
        for comment in comments:
            #only author of 'post' or 'comment' can delete it
            if self.request.POST.get('comment_del') == 'done':
                if (self.request.user == comment.author_comment or self.request.user == post.author_post):
                    comment.delete()

            if self.request.POST.get('comment_like') == 'done':
                #user already liked the comment, delete this like
                if comment.commentlike_set.filter(author_like=self.request.user):
                    c = comment.commentlike_set.get(author_like=self.request.user)
                    c.delete()
                #user like the comment
                else:
                    c = CommentLike.objects.create(author_like=self.request.user,
                                                   liked_comment=comment,
                                                   published_date=timezone.now())

        return redirect('post_detail', pk=post.pk)


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create new Post"""
    template_name = 'Blog/post_new.html'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author_post = self.request.user
        post.published_date = timezone.now()
        send_mail(subject="New Blog",
                  message="you have created a new blog.",
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[self.request.user.email],
                  fail_silently=False)
        post.save()
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    """Create new comment for a post."""
    template_name = 'Blog/post_new.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.author_comment = self.request.user
        comment.post = post
        comment.published_date = timezone.now()
        comment.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """Update Post"""
    template_name = 'Blog/post_new.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        if self.request.user == form.instance.author_post:
            return super().form_valid(form)