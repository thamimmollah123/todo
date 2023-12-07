from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import task


def addtask(request):
     mytask=request.POST['task']
     task.objects.create(task=mytask)
     return redirect('home')

