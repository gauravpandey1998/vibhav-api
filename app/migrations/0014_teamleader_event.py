# Generated by Django 2.1.4 on 2019-01-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190110_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamleader',
            name='event',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
