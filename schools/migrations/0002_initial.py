# Generated by Django 5.0.4 on 2024-04-29 01:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deficiencyreport',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deficiency_reports', to='users.student'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='educational_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='schools.educationalsystem'),
        ),
        migrations.AddField(
            model_name='major',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='majors', to='schools.faculty'),
        ),
        migrations.AddField(
            model_name='class',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='schools.major'),
        ),
        migrations.AddField(
            model_name='semester',
            name='academic_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='schools.academicyear'),
        ),
        migrations.AddField(
            model_name='trainingpoint',
            name='criterion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='schools.criterion'),
        ),
        migrations.AddField(
            model_name='trainingpoint',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='schools.semester'),
        ),
        migrations.AddField(
            model_name='trainingpoint',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='users.student'),
        ),
        migrations.AlterUniqueTogether(
            name='deficiencyreport',
            unique_together={('student', 'activity')},
        ),
    ]
