from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.PostListView.as_view(), name='post_list'),
	path('myfeed/', views.FollowPostListView.as_view(), name='myfeed'),
	path('<int:pk>/myposts/', views.SelfPostListView.as_view(), name='my_post_list'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='post_detail'),
	path('posts/new/', views.PostCreateView.as_view(), name = 'post_new'),
	path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name = 'post_edit'),
	path('posts/<int:pk>/comment/', views.CommentCreateView.as_view(), name = 'post_comment'),
]