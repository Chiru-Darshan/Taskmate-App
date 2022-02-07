from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib import messages

from .models import TaskList


def todoList(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('New Task Added!'))
        return redirect('todoList')

    else:
        all_tasks = TaskList.objects.all()
        return render(request, 'todoList.html', {'tasks': all_tasks})


def contact(request):
    context = {
        'message': 'Welcome to Contacts Page'
    }
    return render(request, 'Contact.html', context)


def about(request):
    context = {
        'message': 'Welcome to About Page'
    }
    return render(request, 'About.html', context)


def delete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    task.delete()
    return redirect("todoList")


def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk = task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Edited Successfully!')
        return redirect("todoList")
    else:
        task = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task': task})
