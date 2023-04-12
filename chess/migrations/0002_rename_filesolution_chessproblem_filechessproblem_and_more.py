# Generated by Django 4.2 on 2023-04-12 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chessproblem',
            old_name='fileSolution',
            new_name='fileChessProblem',
        ),
        migrations.RenameField(
            model_name='chessproblem',
            old_name='imageSolution',
            new_name='imageChessProblem',
        ),
        migrations.RemoveField(
            model_name='chessproblem',
            name='fileSubmit',
        ),
        migrations.RemoveField(
            model_name='chessproblem',
            name='imageSubmit',
        ),
    ]
