from django.shortcuts import render
from django.http import HttpResponse

def becomeamodel(request):
    questions = [float(input("Input your height in meters: ")),
				float(input("Input your weight in kilogram: "))
				]
    return render(request, 'become.html', {'questions': questions})

# height = float(input("Input your height in meters: "))
# weight = float(input("Input your weight in kilogram: "))
# print("Your body mass index is: ", round(weight / (height * height), 2))









# from .models import Question
# from django.shortcuts import redirect
#1
# def qualified_models(request):
#     response_test = redirect('qualified_ok/')
#     return response_test

# def becomeamodel(request):
#     questions = Question.objects.all()
#     return render(request, 'become.html', {'questions': questions})


# def index(request):
#     return HttpResponse("Hello featured model")
# #
# def approve(request):
#     return HttpResponse()
# def disqualified(request):
#     return HttpResponse()

