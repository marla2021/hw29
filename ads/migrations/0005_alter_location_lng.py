# Generated by Django 4.0.2 on 2022-03-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_location_lat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
