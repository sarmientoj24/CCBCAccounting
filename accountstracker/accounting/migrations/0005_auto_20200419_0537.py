# Generated by Django 3.0.5 on 2020-04-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_transaction_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='input_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
