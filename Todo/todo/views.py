from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def markAsDone(request, task_id):
    Task.objects.filter(id=task_id).update(is_completed = True)
    return redirect('home')

def deleteTodo(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('home')

def undoTodo(request, task_id):
    Task.objects.filter(id=task_id).update(is_completed = False)
    return redirect('home')

def editTodo(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'edit_todo.html', {'task': task})

def updateTodo(request, task_id):
    task = request.POST['task']
    Task.objects.filter(id=task_id).update(task=task)
    return redirect('home')