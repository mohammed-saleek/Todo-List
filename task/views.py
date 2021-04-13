from django.shortcuts import render

#for simple HttpResponse
#from django.http import HttpResponse

#For reverse_url
from django.urls import reverse_lazy



#For Class Based views

#For Django Authentication
from django.contrib.auth.views import LoginView
#For listing all tasks
from django.views.generic.list import ListView
#For listing a Specific Task
from django.views.generic.detail import DetailView
#For Creating a Task
from django.views.generic.edit import CreateView
#For Updating a Task
from django.views.generic.edit import UpdateView
#For Deleting a Task
from django.views.generic.edit import DeleteView
#Restricting Pages
from django.contrib.auth.mixins import LoginRequiredMixin

#importing model class
from .models import Task

# Create your views here.

#for functionbased views
#def tasklist(request):
#    return HttpResponse('To Do List')

#Class based views

#Class for Customer Authentication
class CustomLoginView(LoginView):
    template_name = 'task/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

#Class for listing all tasks
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'task/task_list.html'

#Class for listing specific task
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'Task'
    template_name = 'task/task.html'

#Class for creating a task
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    #fileds = ['title','description']
    fields = '__all__'
    success_url = reverse_lazy('tasks')

#Class for updating a Task
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

#Class for deleting a Task
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
