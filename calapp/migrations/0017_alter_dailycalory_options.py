# Generated by Django 5.0.7 on 2024-07-31 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0016_alter_dailycalory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailycalory',
            options={'ordering': ['updated_at']},
        ),
    ]
