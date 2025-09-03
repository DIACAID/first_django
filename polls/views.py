from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You're the polls index")

def results(request, question_id):
    return HttpResponse("Youre looking at question %s" % question_id)