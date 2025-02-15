from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StudySession(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time_spent = models.DurationField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.time_spent}"

class Goal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    reminder_time = models.DateTimeField()

    def __str__(self):
        return f"Reminder for {self.task.title}"

