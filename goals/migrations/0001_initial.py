# Generated by Django 2.0.3 on 2018-03-09 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_title', models.CharField(max_length=30)),
                ('role', models.CharField(choices=[('MTR', 'Mentor'), ('MTE', 'Mentee')], max_length=3)),
                ('score', models.IntegerField(null=True)),
            ],
        ),
    ]