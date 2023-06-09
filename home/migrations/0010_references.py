# Generated by Django 4.2 on 2023-05-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_skills_skill_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('positions', models.CharField(max_length=50)),
                ('org_name', models.CharField(max_length=100)),
                ('pic', models.ImageField(blank=True, upload_to='refer_pic')),
                ('comments', models.TextField(max_length=500)),
            ],
        ),
    ]
