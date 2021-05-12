from django.db import models

# Create your models here.
class Todos(models.Model):
    task=models.CharField(max_length=150)
    date=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100)

    def __str__(self):
        return Todos.task