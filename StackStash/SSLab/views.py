# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
	#orders all question in descending (newest first) order and gets the first 5
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	
	#template = loader.get_template('SSLab/index.html')
	#context = {
	#	'latest_question_list':latest_question_list,
	#}

	#return HttpResponse(template.render(context, request))
	
	return render(request, 'SSLab/index.html', {
		'latest_question_list': latest_question_list
	})

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	
	return render(request, 'SSLab/detail.html', {
	'question': question
	})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	
	return render(request, 'SSLab/results.html', {
	'question': question
	})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting from
		return render(request, 'SSLab/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		
		return HttpResponseRedirect(reverse('SSLab:results', args=(question_id,)))
	
	return HttpResponse("You are voting on question %s." %question_id)
