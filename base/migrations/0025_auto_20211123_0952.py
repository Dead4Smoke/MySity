# Generated by Django 3.1.7 on 2021-11-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_delete_calculate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_1_1',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_1_2',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_1_3',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_1_4',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_1_5',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_2_1',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_2_2',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_2_3',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_2_4',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_3_1',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_3_2',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_3_3',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_3_4',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_3_5',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_4_1',
        ),
        migrations.RemoveField(
            model_name='tablethree',
            name='PP3_4_2',
        ),
        migrations.AddField(
            model_name='tablethree',
            name='PP3_1',
            field=models.TextField(blank=True, choices=[('a1', '???????????? ???????????????? ???? ???????????????????????? ?????????????? ?? ???????????????????????????? ????'), ('a2', '???????????? ???????????????? ???????????????????? ?????????????????????????????????? ??????????????????????'), ('a3', '???????????? ??????????????????-???????????????????????????????? ????????????'), ('a4', '???????????? ???????????????? ?????????????????????? ?????????????????????????????? ???????????????????????????? ???? ???????????????? ?????????? ???? (???????????????? ???????????????????????????? ?? ????????????????)'), ('a5', '???????????? ???????????????? ???????????????? ????????????????????, ???????????????????????? ???? ???????????????????????????? ????')], max_length=100, null=True, verbose_name='???????????????????????????? ????'),
        ),
        migrations.AddField(
            model_name='tablethree',
            name='PP3_2',
            field=models.TextField(blank=True, choices=[('b1', '???????????? ???????????????? ???????????????????? ????????????'), ('b2', '???????????? ???????????????? ???????????????????????????? ?? ??????????????????/????????????/??????????????????/???????????? ?? ?????????????????????????? ?????????????????????????? ????????????????'), ('b3', '???????????? ???????????????? ???? ???????????????????????? ?????????????????????? ???? ?????????????????? ?? ????'), ('b4', '???????????? ???????????????? ???????????????? ????????????????????, ???????????????????????? ???? ???????????????????????? ?? ????')], max_length=100, null=True, verbose_name='????????????????????'),
        ),
        migrations.AddField(
            model_name='tablethree',
            name='PP3_3',
            field=models.TextField(blank=True, choices=[('v1', ' ???????????? ???????????????? ????????????????????/???????????? ?? ???????????????????? ???? ???????????????????? ?????????????????? '), ('v2', ' ???????????? ???????????????? ????????????????????/???????????? ?? ???????????????????? ???? ???????????????????????? ?????????????????? '), ('v3', ' ???????????? ???????????????? ????????????????????/???????????? ?? ???????????????????? ?????????????? '), ('v4', ' ???????????? ???????????????? ?????????????????????? ?????????????????????????????? ???????????????????????????????? ?????????????????? '), ('v5', ' ???????????? ???????????????? ???????????????? ???????????????????? ???????????????????????? ???? ???? ')], max_length=100, null=True, verbose_name='????????????????????????'),
        ),
        migrations.AddField(
            model_name='tablethree',
            name='PP3_4',
            field=models.TextField(blank=True, choices=[('g1', ' ???????????? ???????????????? ???????????????????????????? ?? ???????????????? '), ('g2', ' ???????????? ???????????????? ???????????????????????????? ???? ???????????????? ????????????, ?????? ?????????? ')], max_length=100, null=True, verbose_name='????????????????????????????'),
        ),
    ]
