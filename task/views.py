from django.shortcuts import render

#for simple HttpResponse
#from django.http import HttpResponse

#For Class Based views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

#importing model class
from .models import Task

# Create your views here.

#for functionbased views
#def tasklist(request):
#    return HttpResponse('To Do List')

#Class based views
class TaskList(ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'task/task_list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'Task'
    template_name = 'task/task.html'
