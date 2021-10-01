from . import views
from django.urls import path

urlpatterns = [
	path('user/', views.create_user, name='createUser')
]