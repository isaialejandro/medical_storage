# Generated by Django 3.0.9 on 2020-08-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='active',
            options={'verbose_name': 'Activo de medicamento'},
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Artículo'},
        ),
        migrations.AlterModelOptions(
            name='laboratory',
            options={'verbose_name': 'Laboratorio'},
        ),
        migrations.AlterModelOptions(
            name='lot',
            options={'verbose_name': 'Lote'},
        ),
        migrations.AlterModelOptions(
            name='medcode',
            options={'verbose_name': 'Código de Medicamento'},
        ),
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'Medicamento'},
        ),
        migrations.AlterModelOptions(
            name='medtype',
            options={'verbose_name': 'Tipo de Medicamento'},
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='total_qty',
        ),
        migrations.AddField(
            model_name='medcode',
            name='available_pz',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Piezas disponibles por caja'),
        ),
        migrations.AddField(
            model_name='medcode',
            name='is_new',
            field=models.BooleanField(default=True, verbose_name='Es nuevo?'),
        ),
        migrations.AddField(
            model_name='medcode',
            name='total_pz',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Piezas totales por caja'),
        ),
    ]
