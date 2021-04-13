from django.urls import path

#Routes for function based View
#from . import views

#urlpatterns = [
#    path('', views.tasklist, name = 'task')]

#Routes for Class Based View
from . views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name = 'tasks'),
    path('task/<int:pk>',TaskDetail.as_view(), name = 'task'),
    path('task-create/',TaskCreate.as_view(), name = 'task-create')
]
