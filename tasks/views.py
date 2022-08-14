# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoItemForm
from tasks.models import TodoItem
from django.views import View
from django.views.generic import ListView


def index(request):
    return HttpResponse('Примитивный ответ из приложение tasks')


def complete_task(request, uid): 
    return HttpResponse('Ok')


def delete_task(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.delete()
    return redirect('/tasks/list')

class TaskListView(ListView):
    queryset = TodoItem.objects.all()
    context_object_name = "tasks"
    template_name = "tasks/list.html"


class TaskCreateView(View):
    def post(self, request, *args, **kwargs):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks/list")

        return render(request, "tasks/create.html", {"form": form})
    def get(self, request, *args, **kwargs):
        form = TodoItemForm()
        return render(request, "tasks/create.html", {"form": form})