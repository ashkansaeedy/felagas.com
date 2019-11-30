from django.shortcuts import render
from index.models import Index
from users.models import User


def index_detail(request, pk):
    index = Index.objects.get(pk=pk)
    context = {
        'index' : index
    }
    return render(request, 'index_detail.html' ,context)

def list_of_index(request):
    index_detail = Index.objects.all()
    context = {
        'indexs' : index_detail
    }
    return render(request, 'list_of_index.html' , context)

def index(request):
    return render(request, 'index.html', {})
