# Generated by Django 4.2 on 2023-05-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_experience_to_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='remarks',
            field=models.DateField(blank=True),
        ),
    ]
