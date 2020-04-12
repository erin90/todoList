from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TaskList

def home(request):
    return HttpResponse('Hello World!')

def tasklist(request):
    task_items = TaskList.objects.all()
    return render(request,'tasklist.html',{"all_items":task_items})

def add(request):
    save = TaskList(content=request.POST['value'])
    save.save()
    return HttpResponseRedirect('/')

def delete(request,task_id):
    id = TaskList.objects.get(id=task_id)
    id.delete()
    return HttpResponseRedirect('/')

# Create your views here.
