# Generated by Django 2.1.4 on 2019-01-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_teamleader_team_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='user',
            new_name='admission',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='admission',
            field=models.CharField(default='', max_length=100),
        ),
    ]
