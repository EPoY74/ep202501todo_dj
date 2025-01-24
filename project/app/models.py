from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    shot_task_deskriptions = models.CharField(max_length=30, verbose_name="Описание задачи")
    task_descriptions = models.TextField(verbose_name="Задача")
    due_time = models.DateTimeField(verbose_name="Исполнить до")
    сompleted_date = models.DurationField(blank=True, null=True, verbose_name="Дата выполнения")
    is_done = models.BooleanField(verbose_name="Исполнено")

    def __str__(self):
        return(
            f"{self.autor} | {self.create_at} | {self.shot_task_deskriptions} "
        )
    
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
