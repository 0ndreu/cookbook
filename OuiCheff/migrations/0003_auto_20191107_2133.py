# Generated by Django 2.2.6 on 2019-11-07 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OuiCheff', '0002_receipt_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(default='', max_length=1000)),
                ('calories', models.PositiveIntegerField(default=0)),
                ('proteins', models.PositiveIntegerField(default=0)),
                ('fats', models.PositiveIntegerField(default=0)),
                ('carbohydrates', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='calories',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='receipt',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='receipt',
            name='products',
            field=models.ManyToManyField(to='OuiCheff.Product'),
        ),
    ]
