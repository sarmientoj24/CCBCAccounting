# Generated by Django 3.0.5 on 2020-04-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_auto_20200412_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Single', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_member',
            field=models.CharField(choices=[('Member', 'Member'), ('Visitor', 'Visitor')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1, null=True),
        ),
    ]
