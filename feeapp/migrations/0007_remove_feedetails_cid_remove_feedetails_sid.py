# Generated by Django 4.0.2 on 2022-07-04 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeapp', '0006_alter_feedetails_cid_alter_feedetails_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedetails',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='feedetails',
            name='sid',
        ),
    ]
