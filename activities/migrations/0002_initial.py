# Generated by Django 5.0.4 on 2024-04-29 01:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0001_initial'),
        ('schools', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extracurricularactivity',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activities', to='users.officer'),
        ),
        migrations.AddField(
            model_name='extracurricularactivity',
            name='criterion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activities', to='schools.criterion'),
        ),
        migrations.AddField(
            model_name='extracurricularactivity',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='schools.faculty'),
        ),
        migrations.AddField(
            model_name='extracurricularactivity',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='schools.semester'),
        ),
        migrations.AddField(
            model_name='studentactivityparticipation',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='activities.extracurricularactivity'),
        ),
        migrations.AddField(
            model_name='studentactivityparticipation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participated_activities', to='users.student'),
        ),
        migrations.AddField(
            model_name='extracurricularactivity',
            name='list_of_participants',
            field=models.ManyToManyField(related_name='activities', through='activities.StudentActivityParticipation', to='users.student'),
        ),
        migrations.AlterUniqueTogether(
            name='studentactivityparticipation',
            unique_together={('student', 'activity')},
        ),
    ]
