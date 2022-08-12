# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    return render(request, "tasks/create.html")


def complete_task(request, uid):
    print(uid)
    return HttpResponse('Ok')


def delete_task(request, uid):

    t = TodoItem.objects.get(id=uid)
    t.delete()
    return redirect('/tasks/list')


def add_task(request):
    if request.method == "POST":
        desc = request.POST["description"]
        t = TodoItem(description=desc)
        t.save()
    return redirect("/tasks/list")
