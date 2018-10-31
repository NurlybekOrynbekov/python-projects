from django.db import models
from datetime import datetime

class Table(models.Model):
    table_name = models.CharField(max_length=200)

    def __str__(self):
        return  self.table_name


class Task(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)

    def __str__(self):
        return self.task_text

