# Generated by Django 4.2 on 2023-05-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_myportfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='extrapic')),
            ],
        ),
    ]
