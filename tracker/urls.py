# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_goal/', views.create_goal, name='create_goal'), #working
    path('goal_list/', views.goal_list, name='goal_list'),       #working
    path('create_task/', views.create_task, name='create_task'),       #working
    # path('create_task/<int:goal_id>/', views.create_task, name='create_task'),
    path('task_list/<int:goal_id>/', views.task_list, name='task_list'),
]
