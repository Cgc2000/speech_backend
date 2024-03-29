# Generated by Django 4.2.1 on 2023-06-12 19:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitorSignup',
            fields=[
                ('competitorId', models.IntegerField(primary_key=True, serialize=False)),
                ('schoolKey', models.CharField(max_length=1)),
                ('tournamentId', models.IntegerField()),
                ('registerUserId', models.IntegerField()),
                ('competitorSchool', models.TextField()),
                ('coachName', models.TextField()),
                ('coachEmail', models.TextField()),
                ('coachPhone', models.TextField()),
                ('numEntries', models.IntegerField()),
            ],
            options={
                'db_table': 'speech_competitors',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('entryId', models.IntegerField(primary_key=True, serialize=False)),
                ('studentId', models.IntegerField()),
                ('competitorId', models.IntegerField()),
                ('schoolKey', models.CharField(max_length=1)),
                ('tournamentId', models.IntegerField()),
                ('name', models.TextField()),
                ('event', models.TextField()),
            ],
            options={
                'db_table': 'speech_entries',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TournamentRegister',
            fields=[
                ('tournamentId', models.IntegerField(primary_key=True, serialize=False)),
                ('registerUserId', models.IntegerField()),
                ('tournamentName', models.TextField()),
                ('tournamentLevel', models.TextField()),
                ('hostSchool', models.TextField()),
                ('managerName', models.TextField()),
                ('managerEmail', models.TextField()),
                ('managerPhone', models.TextField()),
                ('tournamentCity', models.TextField()),
                ('tournamentState', models.TextField()),
                ('accessCode', models.TextField()),
                ('schoolsEntered', models.IntegerField()),
                ('events', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
            options={
                'db_table': 'speech_tournaments',
                'managed': True,
            },
        ),
    ]
