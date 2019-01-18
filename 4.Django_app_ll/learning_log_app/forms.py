from django import forms #import form module
from .models import Topic, Entry #import model we will work with

class TopicForm(forms.ModelForm):
	class Meta: #Meta data to tell which model we base the form
		model = Topic #build a form from model
		fields = ['text'] #include only text field
		labels = {'text':''} #generate empty label for field text
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text'] #import field entry
		labels = {'text':''} #blank label
		#single-line textbox, multi-line text area, drop-down list
		widgets = {'text':forms.Textarea(attrs={'cols':80})} #
