from django.test import TestCase
from Blog.models import Post, Like, Comment
from django.utils import timezone
from django.contrib.auth.models import User

class PostModelTest(TestCase):

    def setUp(self):
        #creating object that will same same for all test method
        self.user = User.objects.create_user(username='foo',password='foo_pwd',email='foo@gmail.com')
        self.post = Post.objects.create(author_post=self.user)

    def test_create_author(self):
        self.assertTrue(1,Post.objects.count())
        self.assertEqual(self.post.author_post, Post.objects.get(author_post=self.user).author_post)
        self.post.author_post.save()
        self.assertTrue(1,Post.objects.count())

    def test_publish(self):
        self.assertEqual(None,self.post.published_date)
        self.post.publish()
        self.assertTrue(1,self.post.published_date)


class LikeModelTest(TestCase):

    def setUp(self):
        #creating object that will same same for all test method
        self.user1 = User.objects.create_user(username='foo1',password='foo2_pwd',email='foo1@gmail.com')
        self.user2 = User.objects.create_user(username='foo2',password='foo2_pwd',email='foo2@gmail.com')
        self.post = Post.objects.create(author_post=self.user1)
        self.like = Like.objects.create(author_like=self.user2,liked_post=self.post)

    def test_create_author(self):
        self.assertTrue(1,Like.objects.count())
        self.assertEqual(self.like.author_like, Like.objects.get(author_like=self.user2).author_like)
        self.like.author_like.save()
        self.assertTrue(1,Like.objects.count())

    def test_publish(self):
        self.assertEqual(None,self.post.published_date)
        self.assertTrue(1,self.post.like_set.all().count())
        self.like.publish()
        self.assertTrue(1,self.like.published_date)


class CommentModelTest(TestCase):

    def setUp(self):
        #creating object that will same same for all test method
        self.user1 = User.objects.create_user(username='foo1',password='foo2_pwd',email='foo1@gmail.com')
        self.user2 = User.objects.create_user(username='foo2',password='foo2_pwd',email='foo2@gmail.com')
        self.post = Post.objects.create(author_post=self.user1)
        self.comment = Comment.objects.create(author_comment=self.user2,post=self.post)

    def test_create_author(self):
        self.assertTrue(1,Comment.objects.count())
        self.assertEqual(self.comment.author_comment, Comment.objects.get(author_comment=self.user2).author_comment)
        self.comment.author_comment.save()
        self.assertTrue(1,Comment.objects.count())

    def test_publish(self):
        self.assertEqual(None,self.comment.published_date)
        self.comment.publish()
        self.assertTrue(1,self.comment.published_date)
