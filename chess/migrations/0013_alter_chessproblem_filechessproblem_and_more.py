# Generated by Django 4.2 on 2023-04-19 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0012_chesssolution_matchingchesssolution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chessproblem',
            name='fileChessProblem',
            field=models.FileField(blank=True, null=True, upload_to='texts/chessProblems/'),
        ),
        migrations.AlterField(
            model_name='chesssolution',
            name='fileChessSolution',
            field=models.FileField(blank=True, null=True, upload_to='texts/chessSolutions/'),
        ),
    ]