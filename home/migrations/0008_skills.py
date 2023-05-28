# Generated by Django 4.2 on 2023-05-11 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_educations_cert_imgs_alter_educations_imgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('portfolio_name', models.CharField(blank=True, max_length=100)),
                ('port_file', models.FileField(blank=True, upload_to='')),
                ('port_img', models.ImageField(blank=True, upload_to='portfolio')),
            ],
        ),
    ]