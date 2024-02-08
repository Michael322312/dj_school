 # Introduction
Hello! This repository is example of usage django models. Here I created DB that can create `Teacher`, `Class`, `Subject` and `Student`.
I created very simple interface to interact with DB.

# Start


So first of all lets create django project `school_dj` by writing in terminal:
```Terminal
django-admin startproject school_dj .
```

After that let's create app `school` by this terminal-command:
```
python3 manage.py startapp school
```

Great! We have django-project `school_dj` and django-app `school`

Now lets add in `school_dj/settings.py` our app:
```python
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "school",
]
```

## Creating Models
So open file `school/models.py` (Right now it's empty)

```python
from django.db import models

# Create your models here.
```

After that I created model `Subject` with `name` and `teacher`

```python
class Subject(models.Model):
    name = models.CharField(max_length = 63)
    teacher = models.ManyToManyField("Teacher", related_name="subjects")
```

Then model `Class`:
```python
class Class(models.Model):
    grade = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete = models.DO_NOTHING, default=None)
    teacher = models.ForeignKey("Teacher", on_delete = models.DO_NOTHING, default=None)
```

And two more models `Teacher` and `Student`:
```python

class Teacher(models.Model):
    name = models.CharField(max_length = 63)
    age = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length = 63)
    age = models.IntegerField()
    grade = models.IntegerField()
```
### Making migrations of models
To create migration write in terminal:
```
python3 manage.py makemigrations
```

And after that we need to make migration
```
python3 manage.py migrate
```


# Making Interface
So here I'm gonna add to `main.py` Django-setup:
```python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_dj.settings")
django.setup()
```
After that I created functions with interface:
```python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_dj.settings")
django.setup()


from school.models import Subject, Student, Teacher, Class

def create_subject(name):
    subject = Subject(
        name = name
    )
    subject.save()
    return subject

def create_teacher(name, age):
    teacher = Teacher(
        name = name,
        age = age
    )
    teacher.save()
    return teacher

def create_student(name, age, grade):
    student = Student(
        name = name,
        age=age,
        grade=grade
    )
    student.save()
    return student

def create_class(grade, date, time, subject_id, teacher_id):
    classe = Class(
        grade=grade,
        date=date,
        time=time,
        subject=Subject.objects.get(id=subject_id),
        teacher=Teacher.objects.get(id=teacher_id)
    )
    classe.save()
    return classe

def add_teacher_subject(teacher_id, subject_id):
    teacher = Teacher.objects.get(id=teacher_id)
    subject = Subject.objects.get(id=subject_id)
    subject.teacher.add(teacher)
    subject.save()


while True:
    print("Choose an action:\n1 - Create Subject\n2 - Create Teacher\n3 - Create Student\n4 - Create Class\n5 - Link Teacher to Subject\n6 - Show all teachers\n7 - Show all subjects\n8 - Show clases for date\n0 - Exit\n")
    choise = int(input("Your choice: "))

    match choise:
        case 1:
            name = input("Enter name of the subject\n:")
            create_subject(name)
            print("Subject is successfully created!")
        case 2:
            name = input("Enter name of the teacher:\n")
            age = int(input("Enter age of the teacher:\n"))
            create_teacher(name, age)
            print('The teacher is successfully created!')
        case 3:
            name = input("Enter name of stundent:\n")
            age = int(input("Enter age of the student:\n"))
            grade = int(input("Enter grade of the student:\n"))
            create_student(name, age, grade)
            print("The student created successfully!")
        case 4:
            grade = int(input("Enter grade of the class:\n"))
            date = input("Enter date when class will be (YYYY-MM-DD):\n")
            time = input("Enter time when class will be (HOURS-MINUTES):\n")
            print("\nHere is all subjects:")
            for subject in Subject.objects.all():
                print(f"{subject.id}) {subject.name}")
            subject_id = int(input("Enter subject id: "))
            print("\nHere is full of teachers:")
            for teacher in Teacher.objects.all():
                print(f"{teacher.id}) Name: '{teacher.name}' Age: {teacher.age} Subject:{[i.name for i in teacher.subjects.all()]}")
            teacher_id = int(input("Enter teacher id: "))

            create_class(grade, date, time, subject_id, teacher_id)
            print("Class is successfully created!")
        case 5:
            print("\nHere is full of teachers:")
            for teacher in Teacher.objects.all():
                print(f"{teacher.id}) Name: '{teacher.name}' Age: {teacher.age} Subject:{[i.name for i in teacher.subjects.all()]}")
            teacher_id = int(input("Enter teacher id:"))
            print("\nHere is all subjects:")
            for subject in Subject.objects.all():
                print(f"{subject.id}) {subject.name}")
            subject_id = int(input("Enter subject id: "))
            add_teacher_subject(teacher_id, subject_id)
            print("Subject added to teacher!")
        case 6:
            print("\nHere is full of teachers:")
            for teacher in Teacher.objects.all():
                print(f"{teacher.id}) Name: '{teacher.name}' Age: {teacher.age} Subject:{[i.name for i in teacher.subjects.all()]}")
        case 7:
            print("\nHere is all subjects:")
            for subject in Subject.objects.all():
                print(f"{subject.id}) {subject.name}")
        case 8:
            date = input("Enter date in format(YYYY-MM-DD):\n")
            classes = Class.objects.filter(date=date)
            print("Here are all classes for", date)
            for i in classes:
                print(f"ID - '{i.id}' Time - '{i.time}' Subject - '{i.subject.name}' Teacher - '{i.teacher.name}' Grade - '{i.grade}'")
            
        case 0:
            break
```



