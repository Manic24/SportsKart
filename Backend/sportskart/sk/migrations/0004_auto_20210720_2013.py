# Generated by Django 3.2.5 on 2021-07-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sk', '0003_card_cod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardnum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='cvv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='pin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cod',
            name='pin',
            field=models.IntegerField(),
        ),
    ]
