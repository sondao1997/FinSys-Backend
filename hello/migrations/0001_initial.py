# Generated by Django 3.0.6 on 2020-05-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w', models.FloatField()),
                ('mean12', models.FloatField()),
                ('mean13', models.FloatField()),
                ('mean23', models.FloatField()),
                ('std12', models.FloatField()),
                ('std13', models.FloatField()),
                ('std23', models.FloatField()),
            ],
        ),
    ]
