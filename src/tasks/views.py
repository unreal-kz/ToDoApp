from django.shortcuts import render, redirect

# from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

def index(request):

    tasks = Task.objects.order_by('-created')

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    content = {'tasks': tasks, 'form':form}
    return render(request, 'tasks/index.html', content)


def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect ('/')

    content = {'form':form}

    return render(request, 'tasks/update_task.html', content)


def deleteTask(request,pk):

    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    content = {'item': item}

    return render(request, 'tasks/delete.html', content)