# Generated by Django 4.2 on 2023-05-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('field_name', models.CharField(max_length=150)),
                ('company_name', models.CharField(max_length=200)),
                ('responsibility', models.TextField(max_length=1000)),
                ('from_date', models.DateField(blank=True)),
                ('to_date', models.DateField(blank=True)),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
    ]
