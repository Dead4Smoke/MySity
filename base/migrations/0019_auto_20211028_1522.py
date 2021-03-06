# Generated by Django 3.1.7 on 2021-10-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20211028_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='car9_1',
            field=models.CharField(blank=True, choices=[('0', 'Менее половины населения охвачено системой раннего оповещения.'), ('1', 'Предполагается, что более половины населения может быть охвачено системой раннего оповещения.'), ('2', 'Предполагается, что более 75% населения может быть охвачено системой раннего оповещения.'), ('3', 'Предполагается, что более 90% населения может быть охвачено системой раннего оповещения.')], max_length=10, null=True, verbose_name='П.9.1'),
        ),
        migrations.AddField(
            model_name='card',
            name='car9_2',
            field=models.CharField(blank=True, choices=[('0', 'Нет никакого известного плана.'), ('1', 'Существуют некоторые планы, но они не являются исчерпывающими или не объединены. '), ('2', 'Существует комплексный план, но он содержит значительные пробелы при охвате мер по уменьшению последствий, обеспечению готовности к чрезвычайным ситуациям и реагированию на них. '), ('3', 'Существует план борьбы со стихийными бедствиями / готовности/ реагирования на чрезвычайные ситуации, в котором излагаются меры по уменьшению, обеспечению готовности и реагированию на чрезвычайные ситуации в городе. ')], max_length=10, null=True, verbose_name='П.9.2'),
        ),
        migrations.AddField(
            model_name='card',
            name='car9_3',
            field=models.CharField(blank=True, choices=[('0', 'Нет кадрового потенциала.'), ('1', 'Охват всех районов в течение 48-72 часов.'), ('2', 'Охват всех районов в течение 24-48 часов.'), ('3', 'Кадровый потенциал существует и проверяется либо посредством реальных событий, либо практических упражнений для сценариев бедствий, рассмотренных во 2 принципе - охват всех районов будет возможен в течение 4 часов.')], max_length=10, null=True, verbose_name='П.9.3'),
        ),
        migrations.AddField(
            model_name='card',
            name='car9_4',
            field=models.CharField(blank=True, choices=[('0', 'Потребности не определены (или нет плана).'), ('1', 'Потребности определены условно или есть догадки. '), ('2', 'Определены потребности в соответствии со сценариями бедствий.'), ('3', 'Потребности определяются в соответствии со сценариями бедствий и с учетом роли добровольцев.')], max_length=10, null=True, verbose_name='П.9.4'),
        ),
        migrations.AddField(
            model_name='card',
            name='car9_5',
            field=models.CharField(blank=True, choices=[('0', 'При наиболее опасном сценарии поставка запасных продуктов питания и основных предметов первой помощи меньше, чем предполагаемая потребность на 5% или более/ продовольственный разрыв превышает 24 часа.'), ('1', 'При наиболее опасном сценарии поставка предметов первой необходимости и предметов первой помощи меньше предполагаемой потребности на 2% и более. '), ('2', 'При наиболее опасном сценарии поставка предметов первой необходимости и предметов первой помощи равна расчетной потребности. '), ('3', 'При наиболее опасном сценарии поставки аварийного питания и основных предметов первой необходимости превышают предполагаемую потребность в них.')], max_length=10, null=True, verbose_name='П.9.5'),
        ),
        migrations.AddField(
            model_name='card',
            name='car9_6',
            field=models.CharField(blank=True, choices=[('0', 'Нет центра экстренной помощи.'), ('1', 'Центр экстренной помощи существует, но с уязвимой связью и / или одним или несколькими соответствующими ведомствами не участвующими. '), ('2', 'Центр экстренной помощи существует с укрепленной/резервной связью, предназначенной для борьбы с самым опасным сценарием; только основные ведомства принимают участие. '), ('3', 'Центр экстренной помощи существует с укрепленной/резервной связью, предназначенной для борьбы с самым опасным сценарием; все ведомства принимают участие. ')], max_length=10, null=True, verbose_name='П.9.6'),
        ),
        migrations.AddField(
            model_name='card',
            name='car9_7',
            field=models.CharField(blank=True, choices=[('0', 'Нет тренировок (или нет планов).'), ('1', 'Ситуативные тренировки - не все сценарии проверены, не реалистичны.'), ('2', 'Ежегодные тренировки, утвержденные профессионалами, с ограниченным количеством сценариев.'), ('3', 'Ежегодная тренировка, утвержденная профессионалами, является реалистичным представлением наиболее опасных и наиболее вероятных сценариев.')], max_length=10, null=True, verbose_name='П.9.7'),
        ),
        migrations.AlterField(
            model_name='card',
            name='car6_5',
            field=models.CharField(blank=True, choices=[('0', 'Никакие переводы не были сделаны.'), ('1', 'Все учебные материалы, доступные на некоторых иностранных языках, часто используются в городе.'), ('2', 'Все учебные материалы, доступные на большинстве иностранных языков, часто используются в городе.'), ('3', 'Все учебные материалы, доступные на всех иностранных языках, часто используются в городе.')], max_length=10, null=True, verbose_name='П.6.5'),
        ),
        migrations.AlterField(
            model_name='card',
            name='car6_6',
            field=models.CharField(blank=True, choices=[('0', 'Любой обмен знаниями, который имеет место, зависит от людей.'), ('1', 'Некоторый обмен знаниями происходит между городами, но это носит случайный характер.'), ('2', 'Город понимает важность знаний и имеет членство в ряде городских сетей. Для максимальной выгоды сети не используются.'), ('3', 'Город активно стремится обмениваться знаниями и учиться у других городов, сталкивающихся с аналогичными проблемами, и активно работает в ряде сетей для содействия этому.')], max_length=10, null=True, verbose_name='П.6.6'),
        ),
        migrations.AlterField(
            model_name='card',
            name='car8_5',
            field=models.CharField(blank=True, choices=[('0', 'Значительные потери обслуживания будут при наиболее вероятном сценарии.'), ('1', 'Некоторые потери обслуживания будут при наиболее вероятном сценарии. '), ('2', 'Некоторые потери обслуживания будут при наиболее опасном сценарии. '), ('3', 'Не будет потери обслуживания даже при наиболее опасном сценарии. ')], max_length=10, null=True, verbose_name='П.8.5'),
        ),
        migrations.AlterField(
            model_name='card',
            name='car8_6',
            field=models.CharField(blank=True, choices=[('0', 'Значительные потери обслуживания будут при наиболее вероятном сценарии.'), ('1', 'Некоторые потери обслуживания будут при наиболее вероятном сценарии. '), ('2', 'Некоторые потери обслуживания будут при наиболее опасном сценарии.'), ('3', 'Не будет потери обслуживания даже при наиболее опасном сценарии. ')], max_length=10, null=True, verbose_name='П.8.6'),
        ),
        migrations.AlterField(
            model_name='card',
            name='car8_7',
            field=models.CharField(blank=True, choices=[('0', 'Помощь займет больше 36 часов или отсутствует возможность неотложной медицинской помощи.'), ('1', '>90% основных травм при наиболее опасном сценарии могут быть обработаны в течение 36 часов. '), ('2', '>90% основных травм при наиболее опасном сценарии могут быть обработаны в течение 24 часов. '), ('3', '>90% травм при наиболее опасном сценарии могут быть обработаны в течение 6 часов. ')], max_length=10, null=True, verbose_name='П.8.7'),
        ),
        migrations.AlterField(
            model_name='card',
            name='car8_8',
            field=models.CharField(blank=True, choices=[('0', '>15% учебных заведений подвержены риску при наиболее вероятном сценарии.'), ('1', '5-10% учебных заведений подвержены риску при наиболее вероятном сценарии.'), ('2', 'Никакие учебные заведения не подвержены риску при наиболее вероятном сценарии.'), ('3', 'Никакие учебные заведения не подвержены риску даже при наиболее опасном сценарии. ')], max_length=10, null=True, verbose_name='П.8.8'),
        ),
        migrations.AlterField(
            model_name='card',
            name='car8_9',
            field=models.CharField(blank=True, choices=[('0', 'Значительные пробелы в силах и средствах даже для наиболее вероятного сценария.'), ('1', 'Силы и средства отвечают основным требованиям при наиболее опасном сценарии, но существуют известные пробелы.'), ('2', 'Количество сил и средств либо смоделировано, либо доказано практическим путем, что они соответствуют требованиям при наиболее опасном сценарии, хотя это зависит от договоренностей о взаимопомощи. Соглашения о взаимопомощи проверяются на вероятность быть вовлеченным в одну и ту же катастрофу.'), ('3', 'Количество сил и средств либо смоделировано, либо доказано практическим путем, что они соответствуют требованиям при наиболее опасном сценарии.')], max_length=10, null=True, verbose_name='П.8.9'),
        ),
    ]
