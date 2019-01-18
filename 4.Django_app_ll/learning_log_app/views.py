# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Topic #import the model associated with the data we need
from django.http import HttpResponseRedirect #redirect the reader back to the topics after they submit their topic
from django.core.urlresolvers import reverse #generate an URL from a URL pattern
from .forms import TopicForm, EntryForm
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
def new_topic(request):
	if request.method != 'POST':
		form = TopicForm() #no data submitted => create a blank form
	else:
		form = TopicForm(request.POST) #create a form and pass data from request
		if form.is_valid(): #validate information from the form
			form.save() #save the form to the database
			return HttpResponseRedicrect(reverse('learning_log_app:topics')) #use reverse to get URL for the topics page and pass URL to HttpResponseRedirect()
	context = {'form':form} #on the topics page, the users should see the list of topics that they just entered
	return render(request, 'learning_log_app/new_topic.html', context)