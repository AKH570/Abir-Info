# Generated by Django 4.2 on 2023-05-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_references_email_alter_references_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='port_file',
            field=models.FileField(blank=True, upload_to='vediofile'),
        ),
    ]
