# Generated by Django 3.0.1 on 2020-11-17 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeclock', '0003_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='clockinout',
            name='options',
            field=models.CharField(choices=[('ci', 'Clock In'), ('co', 'Clock Out')], default='ci', max_length=10),
        ),
    ]