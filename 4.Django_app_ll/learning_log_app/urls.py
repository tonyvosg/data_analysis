"""define URL Patterns for learning_logs"""
from django.conf.urls import url #url function - needed when mapping URLs
from . import views
urlpatterns = [
	#Home page
	url(r'^$', views.index, name = 'index'),
	#Show all topics
	url(r'^topics/$', views.topics, name ='topics'),
	#detail pages for single topics 
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
	#page for adding new topic
	#send request to the view function new_topic()
	url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
	#page for adding new entry
	url(r'^new_entry/(?P<topic_id>\d+)$',news.new_entry, name = 'new_entry'),
]