# Generated by Django 2.2.6 on 2019-11-14 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OuiCheff', '0012_auto_20191114_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptHasProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_of_product', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OuiCheff.Product')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OuiCheff.Receipt')),
            ],
        ),
        migrations.DeleteModel(
            name='ReceiptWithProduct',
        ),
    ]
