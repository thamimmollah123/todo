
from django.http import HttpResponse
from django.shortcuts import render
from todos.models import task
def home(request):
     tasks=task.objects.filter(is_completed=False)
     context={
          'tasks':tasks
     }
     return render(request,'home.html',context)