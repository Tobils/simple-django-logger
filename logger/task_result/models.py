from django.db import models

# Create your models here.
class TaskResult(models.Model):
  TaskId = models.CharField(max_length=255, null=True, blank=True)
  Status = models.CharField(max_length=10)
  Result = models.CharField(null=True, max_length=255)
  StackTrace = models.TextField(null=True)
  ResultDate = models.DateTimeField(null=True, blank=True)

  def __str__(self):
      return str(self._get_pk_val()) + " " + str(self.TaskId)
  