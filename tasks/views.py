# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddTaskForm, TodoItemForm

from tasks.models import TodoItem


def index(request):
    return HttpResponse('Примитивный ответ из приложение tasks')


def tasks_list(request):
    all_tasks = TodoItem.objects.all()
    return render(
        request,
        'tasks/list.html',
        {'tasks': all_tasks}
    )


def task_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks/list")
    else:
        form = TodoItemForm()

    return render(request, "tasks/create.html", {"form":form})


def complete_task(request, uid): 
    return HttpResponse('Ok')


def delete_task(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.delete()
    return redirect('/tasks/list')

