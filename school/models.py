from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length = 63)
    teacher = models.ManyToManyField("Teacher", related_name="subjects")


class Class(models.Model):
    name = models.CharField(max_length = 63)

class Teacher(models.Model):
    name = models.CharField(max_length = 63)
    second_name = models.CharField(max_length = 63)


class Student(models.Model):
    name = models.CharField(max_length = 63)


class Schedule(models.Model):
    date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete = models.DO_NOTHING, default = None)
    subject = models.ForeignKey(Subject, on_delete = models.DO_NOTHING, default = None)
    clas = models.ForeignKey(Class, on_delete = models.DO_NOTHING)

    def __str__(self):
        return f"Subject:{self.subject} Class: {self.clas} Date: {self.date} Teacher: {self.teacher}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete = models.DO_NOTHING, default = None)
    schedule = models.ForeignKey(Schedule, on_delete = models.DO_NOTHING, default = None)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
