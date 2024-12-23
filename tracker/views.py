# tracker/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, Task
from .forms import GoalForm, TaskForm

def create_goal(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'tracker/create_goal.html', {'form': form})

def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'tracker/goal_list.html', {'goals': goals})

def create_task(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.method == 'POST':
        # Handle form submission to create a task
        task_name = request.POST['task_name']
        Task.objects.create(goal=goal, name=task_name)
        return redirect('task_list', goal_id=goal.id)
    return render(request, 'create_task.html', {'goal': goal})

# View for displaying tasks related to a specific goal
def task_list(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    tasks = Task.objects.filter(goal=goal)
    return render(request, 'task_list.html', {'goal': goal, 'tasks': tasks})
