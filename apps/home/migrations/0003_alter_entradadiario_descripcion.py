# Generated by Django 3.2.6 on 2021-12-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_entradadiario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradadiario',
            name='descripcion',
            field=models.CharField(blank=True, max_length=220),
        ),
    ]
