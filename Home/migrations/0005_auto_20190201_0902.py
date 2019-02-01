# Generated by Django 2.1.1 on 2019-02-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_product_amazon_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='product',
            name='amazon_url',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
