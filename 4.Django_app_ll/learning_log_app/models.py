# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Topic(models.Model):
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.text
class Entry(models.Model):
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = 'Entries'
	def __str__(self):
		return self.text[:50] + "..."