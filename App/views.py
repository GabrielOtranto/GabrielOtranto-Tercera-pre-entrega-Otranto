from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def hola(request):
    return render(request,'inicio.html')

def create_task(request):
    if request.method == 'GET':
        return render(request, 'ropa.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def registrate(request):
    return render (request,'registrate.html', {
        'form': registro
    } )

def cosmeticos(request):
    return render (request,'cosmeticos.html', {
        'form': cosmetico
    } )