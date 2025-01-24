from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    task_descriptions = models.TextField(verbose_name="Задача")
    due_time = models.DateTimeField(verbose_name="Исполнить до")
    сompleted_date = models.DurationField(verbose_name="Дата выполнения")
    is_done = models.BooleanField(verbose_name="Исполнено")
