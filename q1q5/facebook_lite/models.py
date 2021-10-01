from django.db import models


class User(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField(max_length=254)
	passwordHash = models.CharField(max_length=512)


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	published = models.DateTimeField(auto_now=True)


class Comment(models.Model):
	content = models.CharField(max_length=500)
	published = models.DateTimeField(auto_now=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	parentComment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class Connection(models.Model):
	first = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_user')
	second = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_user')
