from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    context = {
        'tasks': Task.objects.all(),
        'form': TaskForm
    }

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'index.html', context)

def update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'update.html', context)

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {
        'task': task
    }
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', context)
