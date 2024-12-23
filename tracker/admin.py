from django.contrib import admin

# Register your models here.
from .models import Student, Subject, StudySession, Goal, Task, Reminder

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StudySession)
admin.site.register(Goal)
admin.site.register(Task)
admin.site.register(Reminder)
