from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length = 63)
    teacher = models.ForeignKey("Teacher", on_delete = models.DO_NOTHING)

class Class(models.Model):
    grade = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    subject = models.ManyToManyField(Subject, related_name="classes")
    

class Teacher(models.Model):
    name = models.CharField(max_length = 63)
    age = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length = 63)
    age = models.IntegerField()
    grade = models.IntegerField()
    
