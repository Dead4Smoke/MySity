# Generated by Django 3.1.7 on 2021-10-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20211028_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='car3_1',
            field=models.CharField(blank=True, choices=[('0', 'Мало понимания / осведомленности о доступных источниках финансирования СРБ.'), ('1', 'Существует определенный взгляд на пути финансирования, но картина неполна, и мало что делается для того, чтобы заниматься этим.'), ('2', 'Город знает множество путей для обеспечения финансирования деятельности по СРБ и активно следует ряду этих целей.'), ('3', 'Город знает все пути для обеспечения финансирования деятельности по СРБ, активно им следует и добился определенных успехов.')], max_length=10, null=True, verbose_name='П.3.1'),
        ),
        migrations.AddField(
            model_name='card',
            name='car3_2',
            field=models.CharField(blank=True, choices=[('0', ' Существуют значительные пробелы в понимании рисков, даже на уровне отдельных систем (например, энергетика, водоснабжение, транспорт).'), ('1', 'Известны отдельные системные риски, но нет площадки для обсуждений, чтобы поделиться этим или понять каскадный эффект.'), ('2', 'Существует отдельный обмен информацией между городом и различными коммунальными службами и отдельное соглашение по слабым местам.'), ('3', 'Существует общее понимание рисков между городом и различными коммунальными службами – слабые места и взаимозависимости внутри системы.')], max_length=10, null=True, verbose_name='П.3.2'),
        ),
        migrations.AddField(
            model_name='card',
            name='car3_3',
            field=models.CharField(blank=True, choices=[('0', 'Страхование в городе представлено мало или отсутствует.'), ('1', 'Уровень страхование существенно различается по отраслям или по районам. Город мало содействует дальнейшему продвижению страховых продуктов.'), ('2', 'Уровень страхования существенно различается по отраслям или по районам. Город активно стимулирует страховое покрытие по всем отраслям.'), ('3', 'Внедрение страховых услуг во всех сегментах / работах высокая.')], max_length=10, null=True, verbose_name='П.3.3'),
        ),
        migrations.AddField(
            model_name='card',
            name='car3_4',
            field=models.CharField(blank=True, choices=[('0', 'Льгот мало или отсутствуют.'), ('1', 'Существуют отдельные льготы, но неоднородные.'), ('2', 'Существует ряд льгот через все отрасли для повышения устойчивости, но есть еще известные проблемы / возможности.'), ('3', 'Существует ряд льгот через все отрасли для повышения устойчивости и они удовлетворяют известные потребности.')], max_length=10, null=True, verbose_name='П.3.4'),
        ),
    ]