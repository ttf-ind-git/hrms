# Generated by Django 3.2.5 on 2022-02-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0088_alter_onboard_employee_joining_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='onboard_employee',
            name='is_approved',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
