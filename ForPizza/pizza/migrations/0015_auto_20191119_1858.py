# Generated by Django 2.2.7 on 2019-11-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0014_auto_20191119_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='weight',
            field=models.IntegerField(default=50, verbose_name='Weight, grams'),
        ),
        migrations.AlterField(
            model_name='pizza_name',
            name='weight',
            field=models.IntegerField(default=50, verbose_name='Weight, grams'),
        ),
    ]
