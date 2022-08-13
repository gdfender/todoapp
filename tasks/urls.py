from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.TaskListView.as_view(), name='list'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('complete/<int:uid>', views.complete_task, name='complete'),
    path('api/delete/<int:uid>', views.delete_task, name='delete'),
]
