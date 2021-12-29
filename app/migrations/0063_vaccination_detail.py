# Generated by Django 3.2.5 on 2021-12-23 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_auto_20211221_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccination_Detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vaccinated_status', models.CharField(max_length=30)),
                ('vaccin_phase', models.CharField(blank=True, max_length=30, null=True)),
                ('partial_vacci_date', models.DateField(blank=True, null=True)),
                ('date_of_vaccination', models.DateField(blank=True, null=True)),
                ('commends', models.TextField(blank=True, null=True)),
                ('partial_url', models.FileField(blank=True, max_length=500, null=True, upload_to='')),
                ('vaccine_url', models.FileField(blank=True, max_length=500, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.PositiveSmallIntegerField(default=1)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.employee')),
            ],
            options={
                'db_table': 'vaccination_details',
            },
        ),
    ]
