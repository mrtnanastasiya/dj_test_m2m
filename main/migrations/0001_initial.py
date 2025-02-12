# Generated by Django 5.0.6 on 2024-06-16 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('website', models.URLField()),
                ('ppm', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('active', models.BooleanField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='users',
            field=models.ManyToManyField(through='main.Subscription', to='main.user'),
        ),
    ]
