# Generated by Django 5.1.5 on 2025-01-24 18:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('shot_task_deskriptions', models.CharField(max_length=30, verbose_name='Описание задачи')),
                ('task_descriptions', models.TextField(verbose_name='Задача')),
                ('due_time', models.DateTimeField(verbose_name='Исполнить до')),
                ('сompleted_date', models.DurationField(blank=True, default='', verbose_name='Дата выполнения')),
                ('is_done', models.BooleanField(verbose_name='Исполнено')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]
