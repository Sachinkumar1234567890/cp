# Generated by Django 5.0 on 2024-02-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0005_dailycalory_dtype_foodmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailycalory',
            name='dfoodimg',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='foodimg',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]