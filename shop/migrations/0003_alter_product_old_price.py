# Generated by Django 4.0.5 on 2022-06-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_details_alter_product_old_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='price before set discount'),
        ),
    ]
