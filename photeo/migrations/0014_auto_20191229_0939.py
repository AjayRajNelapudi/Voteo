# Generated by Django 2.2.1 on 2019-12-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photeo', '0013_auto_20191215_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='email',
            field=models.EmailField(default='', max_length=128, unique=True),
        ),
    ]
