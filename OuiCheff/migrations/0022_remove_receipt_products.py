# Generated by Django 2.2.6 on 2019-12-04 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OuiCheff', '0021_auto_20191204_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='products',
        ),
    ]
