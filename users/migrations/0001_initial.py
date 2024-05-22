# Generated by Django 4.2.13 on 2024-05-13 08:16

import cloudinary.models
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser',
                 models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avatar', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('role',
                 models.CharField(choices=[('AD', 'Administrator'), ('STU', 'Sinh viên'), ('ASST', 'Trợ lý sinh viên'), ('SPC', 'Chuyên viên cộng tác sinh viên')], default='STU',
                                  max_length=4, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions',
                 models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission',
                                        verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'permissions': [('create_student_account', 'Can create student account'), ('create_assistant_account', 'Can create assistant account'),
                                ('create_specialist_account', 'Can create specialist account')],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ'), ('U', 'Khác')], default='U', max_length=1)),
                ('code', models.CharField(blank=True, db_index=True, editable=False, max_length=10, null=True, unique=True)),
                ('academic_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='schools.academicyear')),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('educational_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='schools.educationalsystem')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='schools.faculty')),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='schools.major')),
                ('sclass', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='schools.class')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ'), ('U', 'Khác')], default='U', max_length=1)),
                ('code', models.CharField(blank=True, db_index=True, editable=False, max_length=10, null=True, unique=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('academic_degree', models.CharField(blank=True, max_length=50, null=True)),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='schools.faculty')),
            ],
            options={
                'verbose_name': 'Specialist',
                'verbose_name_plural': 'Specialists',
            },
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ'), ('U', 'Khác')], default='U', max_length=1)),
                ('code', models.CharField(blank=True, db_index=True, editable=False, max_length=10, null=True, unique=True)),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='schools.faculty')),
            ],
            options={
                'verbose_name': 'Assistant',
                'verbose_name_plural': 'Assistants',
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ'), ('U', 'Khác')], default='U', max_length=1)),
                ('code', models.CharField(blank=True, db_index=True, editable=False, max_length=10, null=True, unique=True)),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='schools.faculty')),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
            },
        ),
    ]