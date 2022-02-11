from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import TaskList

@login_required
def todoList(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request, ('New Task Added!'))
        return redirect('todoList')

    else:

        all_tasks = TaskList.objects.filter(manage= request.user)
        paginator = Paginator(all_tasks, 10)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
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


@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.success(request, 'Not Authorized to Modify Value')
    return redirect("todoList")


@login_required
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


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.success(request, 'Not Authorized to Modify Value')
    return redirect("todoList")


@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.success(request, 'Not Authorized to Modify Value')
    return redirect("todoList")


def home(request):
    return render(request, 'index.html', {})