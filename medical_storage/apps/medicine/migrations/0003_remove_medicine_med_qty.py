# Generated by Django 3.0.9 on 2020-08-07 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_auto_20200807_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='med_qty',
        ),
    ]
