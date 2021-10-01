from django.shortcuts import render
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import bcrypt


# Decorator only allows POST calls on a view
def allow_post_only(f):

	def wrapper(*args, **kwargs):
		if args[0].method == 'POST':
			return f(*args, **kwargs)
		else:
			return HttpResponse(status=405)
	return wrapper


@csrf_exempt
@allow_post_only
def create_user(request):
	userJson = json.loads(request.body)
	user = User.objects.create(name=userJson["name"], 
		email=userJson["email"], passwordHash=bcrypt.hashpw(userJson["password"].encode('utf-8'), bcrypt.gensalt()));
	return HttpResponse(status=204)