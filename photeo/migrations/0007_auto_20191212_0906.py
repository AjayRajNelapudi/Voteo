# Generated by Django 2.2.1 on 2019-12-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photeo', '0006_contestant_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestant',
            name='description',
        ),
        migrations.AddField(
            model_name='contestant',
            name='title',
            field=models.CharField(default=' ', max_length=512),
            preserve_default=False,
        ),
    ]
