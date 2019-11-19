# Generated by Django 2.2.6 on 2019-11-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OuiCheff', '0003_auto_20191107_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='carbohydrates',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='receipt',
            name='fats',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='receipt',
            name='proteins',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]