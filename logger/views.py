from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime

# Create your views here.
import datetime
import logging
logger = logging.getLogger(__name__)

from .task_result.models import TaskResult

@api_view(["POST"])
def test_logger(request):
  __message_logger = "Test was accessed {} dont forget to review !".format(datetime.datetime.now())
  logger.warning(__message_logger)

  task_result = TaskResult(
    TaskId="POST-{}".format(datetime.datetime.now()),
    Status="SUCCESS",
    Result=__message_logger,
    StackTrace=None,
    ResultDate=datetime.datetime.now()
  )
  task_result.save()
  return Response({
    "__msg": __message_logger
  })