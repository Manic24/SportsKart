# Generated by Django 3.2.5 on 2021-07-31 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sk', '0010_delete_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodname', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('addcart', models.CharField(max_length=20)),
            ],
        ),
    ]
