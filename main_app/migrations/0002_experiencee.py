# Generated by Django 5.0.6 on 2024-07-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passsing_year', models.CharField(max_length=300)),
                ('skill', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=400)),
                ('details', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
    ]