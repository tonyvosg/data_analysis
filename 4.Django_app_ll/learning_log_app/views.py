# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Topic #import the model associated with the data we need
# Create your views here
def index(request):
	return render(request, 'learning_log_app/index.html')
def topics(request): 
	topics = Topic.objects.order_by('date_added') #query database and sort by date_added
	#A context is a dictionary in which the keys are names we’ll use in the template to access the data and the values are the data we need to send to the template. 
	context = {'topics':topics}
	return render(request, 'learning_log_app/topics.html', context)
def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries} #store data from database into context
	print(context)
	return render(request, 'learning_log_app/topic.html', context)