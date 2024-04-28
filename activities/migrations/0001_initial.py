# Generated by Django 5.0.4 on 2024-04-28 08:49

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtracurricularActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('organizational_form', models.CharField(choices=[('Onl', 'Online'), ('Off', 'Offline')], default='Off', max_length=3)),
                ('name', models.CharField(max_length=20)),
                ('participant', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('point', models.SmallIntegerField()),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Extracurricular Activities',
                'verbose_name_plural': 'List of extracurricular activities (EA)',
            },
        ),
        migrations.CreateModel(
            name='StudentActivityParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_joined', models.BooleanField(default=False)),
                ('is_point_added', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'EA registration form',
                'verbose_name_plural': 'List of student EA registration forms',
            },
        ),
    ]
