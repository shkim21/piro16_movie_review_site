# Generated by Django 3.2.5 on 2021-11-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('release_date', models.IntegerField(default=1990)),
                ('genre', models.CharField(max_length=50)),
                ('rating', models.FloatField(default=0)),
                ('running_time', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('director', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=255)),
            ],
        ),
    ]
