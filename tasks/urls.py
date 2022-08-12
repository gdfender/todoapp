from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.tasks_list, name='list'),
    path('create/', views.task_create, name='create'),
    path('add-task/', views.task_create, name="api-add-task"),
    path('complete/<int:uid>', views.complete_task, name='complete'),
    path('api/delete/<int:uid>', views.delete_task, name='delete'),
]
