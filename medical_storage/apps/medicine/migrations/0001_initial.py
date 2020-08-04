# Generated by Django 3.0.9 on 2020-08-04 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('laboratory', models.CharField(max_length=100)),
                ('active', models.CharField(max_length=100)),
                ('formule', models.CharField(max_length=100)),
                ('total_qty', models.CharField(max_length=1000, null=True)),
                ('disp_qty', models.CharField(max_length=1000)),
                ('function', models.CharField(max_length=100)),
                ('indications', models.CharField(max_length=100, null=True)),
                ('contraindications', models.CharField(max_length=100)),
                ('cad', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]