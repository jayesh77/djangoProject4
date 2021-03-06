# Generated by Django 3.2 on 2021-04-07 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='Initial_Severity',
            field=models.CharField(choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Fatal', 'Fatal')], default='Mild', max_length=10),
        ),
        migrations.AddField(
            model_name='incident',
            name='location',
            field=models.CharField(choices=[('OD', 'Operations_Department'), ('MD', 'Management_Department'), ('Ad', 'Accounts_Department')], default='Ad', max_length=2),
        ),
    ]
