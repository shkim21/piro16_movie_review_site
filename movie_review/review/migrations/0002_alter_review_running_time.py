# Generated by Django 3.2.6 on 2021-12-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='running_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
