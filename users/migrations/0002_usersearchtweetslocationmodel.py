# Generated by Django 2.0.13 on 2020-08-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSearchTweetsLocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetid', models.IntegerField()),
                ('username', models.CharField(max_length=250)),
                ('userscreenname', models.CharField(max_length=250)),
                ('tweettext', models.CharField(max_length=1500)),
                ('createdat', models.DateTimeField()),
                ('address', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('userloc', models.BooleanField()),
            ],
            options={
                'db_table': 'TweetsTable',
            },
        ),
    ]
