# Generated by Django 4.2 on 2023-04-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0006_alter_chesssolution_imagechesssolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chesssolution',
            name='imageChessSolution',
            field=models.BinaryField(null=True),
        ),
    ]
