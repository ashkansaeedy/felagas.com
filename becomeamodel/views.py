from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# from django.shortcuts import redirect
#1
# def qualified_models(request):
#     response_test = redirect('qualified_ok/')
#     return response_test

def becomeamodel(request):
    questions = Question.objects.all()
    return render(request, 'become.html', {'questions': questions})


# def index(request):
#     return HttpResponse("Hello featured model")
# #
# def approve(request):
#     return HttpResponse()
# def disqualified(request):
#     return HttpResponse()

