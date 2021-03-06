# Generated by Django 3.0.2 on 2020-01-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistressLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='safe_count',
            field=models.IntegerField(default=1),
        ),
    ]
