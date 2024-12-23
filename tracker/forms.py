from django import forms
from .models import Goal, Task

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['student', 'title', 'description', 'deadline']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'completed']
