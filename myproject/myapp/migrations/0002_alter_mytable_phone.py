# Generated by Django 5.1.5 on 2025-02-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytable',
            name='phone',
            field=models.CharField(max_length=80),
        ),
    ]
