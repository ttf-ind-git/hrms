# Generated by Django 3.2.5 on 2022-02-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0082_compoensatory_request_detail_reject_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='reject_reason',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
    ]
