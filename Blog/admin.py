from django.contrib import admin
from .models import Post, Like, Comment, CommentLike, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2', 'email')}), #fields while creating user from admin
    )
    list_display = ['username', 'email']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'follow', 'subscribe')}), #added custom fields to display
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(CommentLike)