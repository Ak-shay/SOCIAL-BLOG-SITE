from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


class CustomUser(AbstractUser):

	follow = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)
	subscribe = models.ManyToManyField('self', related_name='subscribers', symmetrical=False, blank=True)
	#USERNAME_FIELD = 'field which have unique equal to True default is username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.username


class Post(models.Model):
	author_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		# sending email to all subscribers of author
		subscribers = self.author_post.subscribers.all()
		send_mail(subject="New Blog",
				  message=f"A new blog is published by {self.author_post.username}.\n{self.get_absolute_url}",
				  from_email=settings.EMAIL_HOST_USER,
				  recipient_list=[s.email for s in subscribers],
				  fail_silently=False)
		super(Post, self).save(*args, **kwargs)
		


class Like(models.Model):
	author_like = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	published_date = models.DateTimeField(blank=True, null=True)
	liked_post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return self.liked_post.title


class Comment(models.Model):
	author_comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return self.text


class CommentLike(models.Model):
	author_like = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	published_date = models.DateTimeField(blank=True, null=True)
	liked_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

	def __str__(self):
		return self.liked_comment.text
