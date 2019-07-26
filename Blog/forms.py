from django import forms
from .models import Post,Comment, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
