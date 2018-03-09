# Generated by Django 2.0.1 on 2018-02-03 22:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('accounts', '0001_initial'), ('accounts', '0002_auto_20180203_2132'), ('accounts', '0003_auto_20180203_2223')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('interests', models.TextField(blank=True)),
                ('job_years', models.PositiveIntegerField(default=0)),
                ('age_range', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('education_degree', models.CharField(blank=True, max_length=50)),
                ('education_major', models.CharField(blank=True, max_length=50)),
                ('education_school', models.CharField(blank=True, max_length=50)),
                ('education_year_graduated', models.PositiveIntegerField(default=0)),
                ('job_category', models.CharField(blank=True, max_length=50)),
                ('job_level', models.CharField(blank=True, max_length=50)),
                ('job_role', models.CharField(blank=True, max_length=50)),
                ('state_province', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
