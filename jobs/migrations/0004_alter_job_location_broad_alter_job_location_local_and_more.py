# Generated by Django 5.0.4 on 2024-05-01 23:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_location_broad_job_location_local'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Location_Broad',
            field=models.CharField(blank=True, help_text=' City, State, Zip, Territory', max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='Location_Local',
            field=models.CharField(blank=True, help_text='Street', max_length=500),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField()),
                ('Job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Type', models.CharField(choices=[('Assoicate', 'Assoicate'), ('Bacholers', 'Bacholers'), ('Masters', 'Masters'), ('Doctoral', 'Doctoral')], max_length=200)),
                ('Holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
