# Generated by Django 4.0.2 on 2022-06-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('secondname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('course', models.CharField(max_length=25)),
                ('batch', models.CharField(max_length=25)),
            ],
        ),
    ]
