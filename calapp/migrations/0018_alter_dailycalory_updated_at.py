# Generated by Django 5.0.7 on 2024-07-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0017_alter_dailycalory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailycalory',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]