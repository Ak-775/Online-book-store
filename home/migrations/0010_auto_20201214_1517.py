# Generated by Django 3.1.3 on 2020-12-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_orderupdate_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=' ', null=True),
        ),
    ]
