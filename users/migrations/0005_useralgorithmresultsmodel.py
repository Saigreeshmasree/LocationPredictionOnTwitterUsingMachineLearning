# Generated by Django 2.0.13 on 2020-08-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200820_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAlgorithmResultsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('algorithmname', models.CharField(max_length=100)),
                ('accuracy', models.FloatField()),
                ('mae', models.FloatField()),
                ('mse', models.FloatField()),
                ('rmse', models.FloatField()),
                ('r_squared', models.FloatField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'AlgorithmResults',
            },
        ),
    ]
