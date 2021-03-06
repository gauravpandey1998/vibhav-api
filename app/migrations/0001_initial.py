# Generated by Django 2.0.10 on 2019-01-15 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default='', max_length=1500)),
                ('rules', models.CharField(default='', max_length=1500)),
                ('judging', models.CharField(default='', max_length=1500)),
                ('prizes', models.CharField(default='', max_length=1500)),
                ('contacts', models.CharField(default='', max_length=1500)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(default='', max_length=30)),
                ('average_rating', models.CharField(default='0', max_length=20)),
                ('number_of_rates', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(default='', max_length=100)),
                ('team_name', models.CharField(default='', max_length=50)),
                ('admission', models.CharField(default='', max_length=100)),
                ('token', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_event', models.CharField(default='', max_length=100)),
                ('team_name', models.CharField(default='', max_length=100)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_leader', models.CharField(default='0', max_length=100)),
                ('team_name', models.CharField(default='0', max_length=100)),
                ('adm_no', models.CharField(default='0', max_length=100)),
                ('phone', models.CharField(default='0', max_length=100)),
                ('event', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=13)),
                ('name', models.CharField(default='', max_length=100)),
                ('branch', models.CharField(default='', max_length=100)),
                ('coins', models.IntegerField(default=500)),
                ('admission', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('imageurl', models.CharField(default='https://i.stack.imgur.com/l60Hf.png', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aaviskar', models.CharField(default='0', max_length=20)),
                ('technovation', models.CharField(default='0', max_length=20)),
                ('codee', models.CharField(default='0', max_length=20)),
                ('buffet_money', models.CharField(default='0', max_length=20)),
                ('robo_soccer', models.CharField(default='0', max_length=20)),
                ('lazer_maze', models.CharField(default='0', max_length=20)),
                ('placement_fever', models.CharField(default='0', max_length=20)),
                ('cs_go', models.CharField(default='0', max_length=20)),
                ('auction_villa', models.CharField(default='0', max_length=20)),
                ('treasure_hunt', models.CharField(default='0', max_length=20)),
                ('marketing_roadies', models.CharField(default='0', max_length=20)),
                ('sherlocked', models.CharField(default='0', max_length=20)),
                ('pubg', models.CharField(default='0', max_length=20)),
                ('guest_lecture', models.CharField(default='0', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aaviskar', models.CharField(default='0', max_length=20)),
                ('technovation', models.CharField(default='0', max_length=20)),
                ('codee', models.CharField(default='0', max_length=20)),
                ('buffet_money', models.CharField(default='0', max_length=20)),
                ('robo_soccer', models.CharField(default='0', max_length=20)),
                ('lazer_maze', models.CharField(default='0', max_length=20)),
                ('placement_fever', models.CharField(default='0', max_length=20)),
                ('cs_go', models.CharField(default='0', max_length=20)),
                ('auction_villa', models.CharField(default='0', max_length=20)),
                ('treasure_hunt', models.CharField(default='0', max_length=20)),
                ('marketing_roadies', models.CharField(default='0', max_length=20)),
                ('sherlocked', models.CharField(default='0', max_length=20)),
                ('pubg', models.CharField(default='0', max_length=20)),
                ('guest_lecture', models.CharField(default='0', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
