# Generated by Django 4.2 on 2023-04-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('hint', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('solved', models.BooleanField(default=False)),
            ],
        ),
    ]