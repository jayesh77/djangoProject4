# Generated by Django 3.2 on 2021-04-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20210408_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='Date_and_Time_of_incident',
        ),
        migrations.AlterField(
            model_name='incident',
            name='location',
            field=models.CharField(choices=[('OD', 'Operations Department'), ('MD', 'Management Department'), ('Ad', 'Accounts Department')], default='Ad', max_length=2),
        ),
    ]