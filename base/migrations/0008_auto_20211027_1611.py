# Generated by Django 3.1.7 on 2021-10-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20211027_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableone',
            name='A8_1',
            field=models.TextField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
        migrations.AlterField(
            model_name='tableone',
            name='A8_2',
            field=models.TextField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
        migrations.AlterField(
            model_name='tableone',
            name='A8_3',
            field=models.TextField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
        migrations.AlterField(
            model_name='tableone',
            name='A8_4',
            field=models.TextField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
        migrations.AlterField(
            model_name='tableone',
            name='A8_5',
            field=models.TextField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
    ]