from django.contrib import admin
#Importing Task app model class
from .models import Task

# Register your models here.
admin.site.register(Task)
