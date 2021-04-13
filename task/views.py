from django.shortcuts import render

#for simple HttpResponse
#from django.http import HttpResponse

#For Class Based views

#For listing all tasks
from django.views.generic.list import ListView
#For listing a Specific Task
from django.views.generic.detail import DetailView
#For Creating a Task
from django.views.generic.edit import CreateView
#For reverse_url
from django.urls import reverse_lazy

#importing model class
from .models import Task

# Create your views here.

#for functionbased views
#def tasklist(request):
#    return HttpResponse('To Do List')

#Class based views

#Class for listing all tasks
class TaskList(ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'task/task_list.html'

#Class for listing specific task
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'Task'
    template_name = 'task/task.html'

#Class for creating a task
class TaskCreate(CreateView):
    model = Task
    #fileds = ['title','description']
    fields = '__all__'
    success_url = reverse_lazy('tasks')
