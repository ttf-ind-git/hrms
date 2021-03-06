# Generated by Django 3.2.5 on 2021-10-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_alter_announcement_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar_Detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('event_type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'calendar_details',
            },
        ),
        migrations.CreateModel(
            name='Holiday_Detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('holiday_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(max_length=30)),
                ('applicable_location', models.CharField(blank=True, max_length=450, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'holiday_details',
            },
        ),
    ]
