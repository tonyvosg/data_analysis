"""define URL Patterns for learning_logs"""
from django.conf.urls import url #url function - needed when mapping URLs
from . import views
urlpatterns = [
	#Home page
	url(r'^$', views.index, name = 'index'),
	#Show all topics
	url(r'^topics/$', views.topics, name ='topics'),
	#detail pages for single topics 
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic')
]