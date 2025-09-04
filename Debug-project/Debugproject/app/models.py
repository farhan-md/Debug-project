from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    # Intentionally wrong: its name should be age
    agee = models.IntegerField(default=18)