# Generated by Django 3.2.5 on 2022-01-04 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0072_auto_20220104_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset_detail',
            name='is_approved',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='asset_detail',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asset_approve', to='app.employee'),
        ),
    ]
