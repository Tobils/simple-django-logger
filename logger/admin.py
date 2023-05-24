from django.contrib import admin

# Register your models here.
from .task_result.models import TaskResult

admin.site.register(TaskResult)