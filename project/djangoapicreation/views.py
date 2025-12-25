from django.shortcuts import render
from .models import Question
from django.http import HttpResponse
from django.template import loader
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    template = loader.get_template('djangoapicreation/index.html')
    context = {
        'latest_documents' : latest_question_list,
    }
    return HttpResponse(template.render(context,request))
def details(request, question_id):
    return HttpResponse(f"You're Looking at question id {question_id}")
def results(request, question_id):
    response = "You're looking at the result of question"
    return HttpResponse(f"{response} { question_id}")
def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")