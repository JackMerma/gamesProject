# Generated by Django 4.2 on 2023-04-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0010_alter_chesssolution_imagechesssolution'),
    ]

    operations = [
        migrations.AddField(
            model_name='chesssolution',
            name='codeChessSolution',
            field=models.TextField(default='idk'),
            preserve_default=False,
        ),
    ]
