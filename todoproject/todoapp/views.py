from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages

# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('-id')
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    
    return render(request, 'todoapp/index.html', {'tasks': tasks, 'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
    return redirect('index')

def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
        status = 'completed' if task.completed else 'marked as pending'
        messages.success(request, f'Task {status}!')
    return redirect('index')


