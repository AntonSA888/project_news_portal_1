from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from news.resources import *


class Author(models.Model):
    author_rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        sum_post_rating = Post.objects.filter(author=self).aggregate(Sum('post_rating')) * 3
        sum_author_comment_rating = Comment.objects.filter(user=self).aggregate(Sum('comment_rating'))
        sum_comment_rating = Comment.objects.filter(post=Post.author(self)).aggregate(Sum('comment_rating'))
        self.author_rating = sum_post_rating + sum_author_comment_rating + sum_comment_rating


class Category(models.Model):
    category = models.CharField(max_length=2, choices=CATEGORIES, default=other, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPES) #news = 'NW' article = 'AR'
    post_datetime = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        if self.post_rating > 0:
            self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post_text[:124]+'...'

    # def finish_order(self):
    #     self.time_out = datetime.now()
    #     self.complete = True
    #     self.save()
    #

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=4098)
    comment_datetime = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        if self.comment_rating > 0:
            self.comment_rating -= 1
        self.save()
