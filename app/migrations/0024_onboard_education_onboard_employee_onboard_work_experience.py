# Generated by Django 3.2.5 on 2021-09-24 06:03

import app.models.onboard_employee_model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onboard_Employee',
            fields=[
                ('candidate_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=50)),
                ('code_name', models.CharField(blank=True, max_length=50, null=True)),
                ('code_num', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_number', models.CharField(max_length=12)),
                ('official_email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('emirate_id', models.CharField(blank=True, max_length=50, null=True)),
                ('photo_url', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('experience', models.CharField(blank=True, max_length=20, null=True)),
                ('source_of_hire', models.CharField(blank=True, max_length=200, null=True)),
                ('skill_set', models.CharField(blank=True, max_length=250, null=True)),
                ('highest_qualify', models.CharField(blank=True, max_length=250, null=True)),
                ('additional_info', models.CharField(blank=True, max_length=550, null=True)),
                ('current_sal', models.CharField(blank=True, max_length=550, null=True)),
                ('offer_letter_url', models.CharField(blank=True, max_length=550, null=True)),
                ('tentative_joining_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'onboard_employee',
            },
        ),
        migrations.CreateModel(
            name='Onboard_Work_Experience',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('previous_company_name', models.CharField(blank=True, max_length=180, null=True)),
                ('job_title', models.CharField(blank=True, max_length=180, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('job_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_active', models.PositiveSmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.onboard_employee')),
            ],
            options={
                'db_table': 'onboard_work_experience',
            },
        ),
        migrations.CreateModel(
            name='Onboard_Education',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(blank=True, max_length=180, null=True)),
                ('degree', models.CharField(blank=True, max_length=180, null=True)),
                ('field', models.CharField(blank=True, max_length=180, null=True)),
                ('date_of_completion', models.DateField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=1000, null=True)),
                ('interests', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_active', models.PositiveSmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.onboard_employee')),
            ],
            options={
                'db_table': 'onboard_education',
            },
        ),
    ]
