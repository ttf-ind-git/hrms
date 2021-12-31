# Generated by Django 3.2.5 on 2021-12-17 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_alter_leave_balance_total_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='checkin_lang',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='checkin_lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='checkin_location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='checkout_lang',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='checkout_lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='checkout_location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='passport_exp_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='passport_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='psssport_url',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='subject',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_emp', to='app.location'),
        ),
    ]