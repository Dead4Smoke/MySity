# Generated by Django 3.1.7 on 2021-11-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_auto_20211126_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableone',
            name='A6_2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Численность населения, охваченного системами оповещения (тыс.чел %) от общей численности населения территории'),
        ),
    ]
