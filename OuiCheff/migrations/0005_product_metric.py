# Generated by Django 2.2.6 on 2019-11-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OuiCheff', '0004_auto_20191107_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='metric',
            field=models.CharField(choices=[('л', 'литры'), ('кг', 'килограммы'), ('шт', 'штуки')], max_length=2, null=True),
        ),
    ]
