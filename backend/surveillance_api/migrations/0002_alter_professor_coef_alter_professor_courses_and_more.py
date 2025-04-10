# Generated by Django 4.2 on 2025-04-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveillance_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='coef',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='courses',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='max_surveillance_hours',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='td',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='tp',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
