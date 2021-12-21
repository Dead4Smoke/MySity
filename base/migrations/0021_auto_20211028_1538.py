# Generated by Django 3.1.7 on 2021-10-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20211028_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='car1_1',
            field=models.CharField(blank=True, choices=[('0', 'Нет плана / нет соответствия'), ('1', 'Планы, предлагающиечастичное соответствие Сендайской рамочной программе и охватывающие часть из 10 прнципов.'), ('2', 'Отдельный план по СРБ, соответствующий Сендайской рамочной программы и решению всех 10 принципов.'), ('3', 'Полностью интегрированный план Снижения риска бедстви (СРБ), полный охват Сендайской рамочной программы по всем 10 принципам.')], max_length=10, null=True, verbose_name='П.1.1'),
        ),
    ]
