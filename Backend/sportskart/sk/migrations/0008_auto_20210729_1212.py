# Generated by Django 3.2.5 on 2021-07-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sk', '0007_rename_cod_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='expmon',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='state',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cash',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cash',
            name='state',
            field=models.CharField(max_length=20),
        ),
    ]
