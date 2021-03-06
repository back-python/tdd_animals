# Generated by Django 4.0.3 on 2022-03-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=100, unique=True)),
                ('venomous', models.BooleanField()),
                ('predator', models.BooleanField()),
                ('domestic', models.BooleanField()),
            ],
        ),
    ]
