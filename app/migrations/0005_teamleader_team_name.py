# Generated by Django 2.1.4 on 2019-01-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_registrationmanagement_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamleader',
            name='team_name',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
