# Generated by Django 3.0.1 on 2020-11-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeclock', '0004_clockinout_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('notes', models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
        migrations.AlterField(
            model_name='clockinout',
            name='options',
            field=models.CharField(choices=[('CLOCKED IN AT ', 'Clock In'), ('CLOCKED OUT AT', 'Clock Out')], default='Clocked in at', max_length=14),
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
    ]