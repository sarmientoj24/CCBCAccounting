# Generated by Django 3.0.5 on 2020-04-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_auto_20200419_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='care',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='choir',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='circle_of_faith',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='creative_team',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='dvbs',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='firstfruit',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='firstfruit_year',
            field=models.PositiveIntegerField(blank=True, default='2020'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='input_date',
            field=models.DateField(blank=True, default='2020-04-19'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='ladies',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='men',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mission',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='offering',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='others',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='prayer_breakfast',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='prison_ministry',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tithe',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='youth',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
