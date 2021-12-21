# Generated by Django 3.1.7 on 2021-10-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20211028_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='car4_1',
            field=models.CharField(blank=True, choices=[('0', 'Зонирование не четкое / отсутствует.'), ('1', 'Зонирование не является полным и нерегулярно пересматривается в отношении опасностей / рисков.'), ('2', 'Город разбит на зоны по землепользованию, и это слабо сочетается с опасностями и картированием рисков (см. принцип 2). Планы по обновлению это зонирование не вполне понятны.'), ('3', 'Город разбит на зоны по землепользованию, и это хорошо соединено с опасностями и картированием рисков (см. принцип 2). Зонирование обновляется через согласованные промежутки времени.')], max_length=10, null=True, verbose_name='П.4.1'),
        ),
        migrations.AddField(
            model_name='card',
            name='car4_2',
            field=models.CharField(blank=True, choices=[('0', 'Мало / нет продвижения устойчивости в новом городском развитии.'), ('1', 'Подходы к повышению устойчивости продвигаются, но непоследовательно и не подкрепляются городской политикой.'), ('2', 'Политика существует, но вспомогательные методические рекомендации неполные.'), ('3', 'Четкая политика существует на уровне города. Методические рекомендации подготовлены для ряда практиков (например, архитекторов, ландшафтных архитекторов, инженеров и т. д.).')], max_length=10, null=True, verbose_name='П.4.2'),
        ),
        migrations.AddField(
            model_name='card',
            name='car4_3',
            field=models.CharField(blank=True, choices=[('0', 'Не существуют / не используются соответствующие строительные норм и стандартов.'), ('1', 'Существуют некоторые нормы, охватывающие некоторые опасности. Нет четкого плана обновления норм и стандартов.'), ('2', 'Существуют местные нормы и стандарты; они касаются основных известных опасностей города и регулярно обновляются.'), ('3', 'Существуют местные нормы и стандарты; они касаются всех известных опасностей города и регулярно обновляются.')], max_length=10, null=True, verbose_name='П.4.3'),
        ),
        migrations.AddField(
            model_name='card',
            name='car4_4',
            field=models.CharField(blank=True, choices=[('0', 'Не уделяется внимание реализации правил зонирования и строительных норм.'), ('1', 'Применение существующих правил зонирования и строительных норм является частичным и/или непоследовательным.'), ('2', 'Правила зонирования и строительные нормы проверяются и применяются в 50% случав.'), ('3', 'Правила зонирования и строительные нормы проверяются и применяются на 100% .')], max_length=10, null=True, verbose_name='П.4.4'),
        ),
    ]
