# Generated by Django 3.2.5 on 2021-08-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_leave_effective_reset_carry_forward_overall_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='code_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='code_num',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
