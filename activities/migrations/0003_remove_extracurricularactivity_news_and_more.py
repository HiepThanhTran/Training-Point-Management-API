# Generated by Django 5.0.4 on 2024-04-28 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extracurricularactivity',
            name='news',
        ),
        migrations.AlterModelOptions(
            name='extracurricularactivity',
            options={'verbose_name': 'Extracurricular Activities', 'verbose_name_plural': 'List of extracurricular activities (EA)'},
        ),
        migrations.AlterModelOptions(
            name='studentactivityparticipation',
            options={'verbose_name': 'EA registration form', 'verbose_name_plural': 'List of student EA registration forms'},
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]