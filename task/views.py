from django.shortcuts import render, redirect

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
#For Creating a Form
from django.views.generic.edit import FormView
#For Creating User
from django.contrib.auth.forms import UserCreationForm
#For directly logging in the created user
from django.contrib.auth import login

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

#Class For Customer Registration
class RegisterPage(FormView):
    template_name = 'task/register.html'
    #User Registration Form
    form_class = UserCreationForm
    #For redirecting authenticated user
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    #Saving User
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    #Manually redirecting an authenticated user
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

#Class for listing all tasks
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'task/task_list.html'

    #To get user-specific data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Context data
        #context['colour'] = 'red'
        #in html page use : {{colour}}
        context['Tasks'] = context['Tasks'].filter(user = self.request.user)
        context['count'] = context['Tasks'].filter(complete = False).count()

        #For search option
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['Tasks'] = context['Tasks'].filter(title__startswith = search_input)
        #For the value to stay in the search box even after searching
        #add value to the text input as "{{search_input}}"
        context['search_input'] = search_input
        return context

#Class for listing specific task
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'Task'
    template_name = 'task/task.html'

#Class for creating a task
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description','complete']
    #fields = '__all__'
    success_url = reverse_lazy('tasks')

    #Only a User Can Create Task for them and not for others, restriction
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

#Class for updating a Task
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','description','complete']
    #fields = '__all__'
    success_url = reverse_lazy('tasks')

#Class for deleting a Task
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
