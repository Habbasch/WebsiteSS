# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question

# Create your views here.

def index(request):
	#orders all question in descending (newest first) order and gets the first 5
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list':latest_question_list,
	}

	return render(request, 'SSLab/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'SSLab/detail.html', {'question': question})

def results(request, question_id):
	response = "You are looking at the results of question %s."
	return HttpResponse(response %question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s." %question_id)
