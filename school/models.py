from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length = 63)
    teacher = models.ManyToManyField("Teacher", related_name="subjects")

class Class(models.Model):
    grade = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete = models.DO_NOTHING, default=None)
    teacher = models.ForeignKey("Teacher", on_delete = models.DO_NOTHING, default=None)

class Teacher(models.Model):
    name = models.CharField(max_length = 63)
    age = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length = 63)
    age = models.IntegerField()
    grade = models.IntegerField()
    
