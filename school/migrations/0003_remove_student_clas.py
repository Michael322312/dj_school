# Generated by Django 5.0.1 on 2024-02-10 10:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0002_remove_student_classes_student_clas"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="clas",
        ),
    ]
