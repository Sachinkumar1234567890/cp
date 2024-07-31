# Generated by Django 5.0 on 2024-02-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0003_rename_img_foodmodel_foodimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='dailycalory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=100)),
                ('dquantity', models.FloatField()),
                ('dprotein', models.FloatField()),
                ('dcarbs', models.FloatField()),
                ('dfat', models.FloatField()),
                ('dnutrients', models.FloatField()),
                ('dvitamins', models.CharField(max_length=100)),
                ('dfoodimg', models.ImageField(blank=True, upload_to='foodimage/')),
            ],
        ),
    ]