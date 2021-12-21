# Generated by Django 3.1.7 on 2021-10-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableone',
            name='A10_2017',
            field=models.IntegerField(null=True, verbose_name='Смертность населения трудоспособного возраста (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A10_2018',
            field=models.IntegerField(null=True, verbose_name='Смертность населения трудоспособного возраста (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A10_2019',
            field=models.IntegerField(null=True, verbose_name='Смертность населения трудоспособного возраста (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A10_2020',
            field=models.IntegerField(null=True, verbose_name='Смертность населения трудоспособного возраста (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A11_2017',
            field=models.IntegerField(null=True, verbose_name='Смертность от ДТП (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A11_2018',
            field=models.IntegerField(null=True, verbose_name='Смертность от ДТП (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A11_2019',
            field=models.IntegerField(null=True, verbose_name='Смертность от ДТП (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A11_2020',
            field=models.IntegerField(null=True, verbose_name='Смертность от ДТП (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A12_2017',
            field=models.IntegerField(null=True, verbose_name='Количество погибших при авариях и происшествиях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A12_2018',
            field=models.IntegerField(null=True, verbose_name='Количество погибших при авариях и происшествиях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A12_2019',
            field=models.IntegerField(null=True, verbose_name='Количество погибших при авариях и происшествиях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A12_2020',
            field=models.IntegerField(null=True, verbose_name='Количество погибших при авариях и происшествиях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A13_2017',
            field=models.IntegerField(null=True, verbose_name='Количество населения, погибшего в чрезвычайных ситуациях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A13_2018',
            field=models.IntegerField(null=True, verbose_name='Количество населения, погибшего в чрезвычайных ситуациях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A13_2019',
            field=models.IntegerField(null=True, verbose_name='Количество населения, погибшего в чрезвычайных ситуациях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A13_2020',
            field=models.IntegerField(null=True, verbose_name='Количество населения, погибшего в чрезвычайных ситуациях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A14_2017',
            field=models.IntegerField(null=True, verbose_name='Количество людей, погибших в результате пожара (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A14_2018',
            field=models.IntegerField(null=True, verbose_name='Количество людей, погибших в результате пожара (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A14_2019',
            field=models.IntegerField(null=True, verbose_name='Количество людей, погибших в результате пожара (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A14_2020',
            field=models.IntegerField(null=True, verbose_name='Количество людей, погибших в результате пожара (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A15_2017',
            field=models.IntegerField(null=True, verbose_name='Количество погибших в происшествиях на водных объектах '),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A15_2018',
            field=models.IntegerField(null=True, verbose_name='Количество погибших в происшествиях на водных объектах '),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A15_2019',
            field=models.IntegerField(null=True, verbose_name='Количество погибших в происшествиях на водных объектах '),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A15_2020',
            field=models.IntegerField(null=True, verbose_name='Количество погибших в происшествиях на водных объектах '),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A16_2017',
            field=models.IntegerField(null=True, verbose_name='Количество населения, пострадавшего в чрезвычайных ситуациях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A16_2018',
            field=models.IntegerField(null=True, verbose_name='Количество населения, пострадавшего в чрезвычайных ситуациях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A16_2019',
            field=models.IntegerField(null=True, verbose_name='Количество населения, пострадавшего в чрезвычайных ситуациях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A16_2020',
            field=models.IntegerField(null=True, verbose_name='Количество населения, пострадавшего в чрезвычайных ситуациях (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A17_2017',
            field=models.IntegerField(null=True, verbose_name='Количество людей, травмированных в результате пожаров (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A17_2018',
            field=models.IntegerField(null=True, verbose_name='Количество людей, травмированных в результате пожаров (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A17_2019',
            field=models.IntegerField(null=True, verbose_name='Количество людей, травмированных в результате пожаров (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A17_2020',
            field=models.IntegerField(null=True, verbose_name='Количество людей, травмированных в результате пожаров (чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A18_2017',
            field=models.IntegerField(null=True, verbose_name='Количество ЧС природного характера, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A18_2018',
            field=models.IntegerField(null=True, verbose_name='Количество ЧС природного характера, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A18_2019',
            field=models.IntegerField(null=True, verbose_name='Количество ЧС природного характера, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A18_2020',
            field=models.IntegerField(null=True, verbose_name='Количество ЧС природного характера, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A19_2017',
            field=models.IntegerField(null=True, verbose_name='Количество ЧС техногенного характера, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A19_2018',
            field=models.IntegerField(null=True, verbose_name='Количество ЧС техногенного характера, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A19_2019',
            field=models.IntegerField(null=True, verbose_name='Количество ЧС техногенного характера, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A19_2020',
            field=models.IntegerField(null=True, verbose_name='Количество ЧС техногенного характера, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A1_2017',
            field=models.IntegerField(null=True, verbose_name='Численность постоянного населения на 1 января текущего года (тыс. чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A1_2018',
            field=models.IntegerField(null=True, verbose_name='Численность постоянного населения на 1 января текущего года (тыс. чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A1_2019',
            field=models.IntegerField(null=True, verbose_name='Численность постоянного населения на 1 января текущего года (тыс. чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A1_2020',
            field=models.IntegerField(null=True, verbose_name='Численность постоянного населения на 1 января текущего года (тыс. чел.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A20_2017',
            field=models.IntegerField(null=True, verbose_name='Количество пожаров, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A20_2018',
            field=models.IntegerField(null=True, verbose_name='Количество пожаров, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A20_2019',
            field=models.IntegerField(null=True, verbose_name='Количество пожаров, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A20_2020',
            field=models.IntegerField(null=True, verbose_name='Количество пожаров, в которых погибло 10 и более человек'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A2_2017',
            field=models.IntegerField(null=True, verbose_name='Количество лечебно-профилактической организации (ед.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A2_2018',
            field=models.IntegerField(null=True, verbose_name='Количество лечебно-профилактической организации (ед.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A2_2019',
            field=models.IntegerField(null=True, verbose_name='Количество лечебно-профилактической организации (ед.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A2_2020',
            field=models.IntegerField(null=True, verbose_name='Количество лечебно-профилактической организации (ед.)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A3_2017',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных дошкольных образовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A3_2018',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных дошкольных образовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A3_2019',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных дошкольных образовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A3_2020',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных дошкольных образовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A4_2017',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных общеобразовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A4_2018',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных общеобразовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A4_2019',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных общеобразовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A4_2020',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных общеобразовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A5_2017',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных учереждений культуры организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A5_2018',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных учереждений культуры организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A5_2019',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных учереждений культуры организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A5_2020',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных учереждений культуры организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A6_2017',
            field=models.IntegerField(null=True, verbose_name='Численность населения, охваченного системами оповещения (тыс.чел %) от общей численности населения территории'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A6_2018',
            field=models.IntegerField(null=True, verbose_name='Численность населения, охваченного системами оповещения (тыс.чел %) от общей численности населения территории'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A6_2019',
            field=models.IntegerField(null=True, verbose_name='Численность населения, охваченного системами оповещения (тыс.чел %) от общей численности населения территории'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A6_2020',
            field=models.IntegerField(null=True, verbose_name='Численность населения, охваченного системами оповещения (тыс.чел %) от общей численности населения территории'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A7_2017',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Наличие утвержденного документа территориальногшо планирования'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A7_2018',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Наличие утвержденного документа территориальногшо планирования'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A7_2019',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Наличие утвержденного документа территориальногшо планирования'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A7_2020',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Наличие утвержденного документа территориальногшо планирования'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A8_2017',
            field=models.IntegerField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A8_2018',
            field=models.IntegerField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A8_2019',
            field=models.IntegerField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A8_2020',
            field=models.IntegerField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования '),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A9_2017',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Степень износа жилого фонда (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A9_2018',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Степень износа жилого фонда (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A9_2019',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Степень износа жилого фонда (%)'),
        ),
        migrations.AddField(
            model_name='tableone',
            name='A9_2020',
            field=models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Степень износа жилого фонда (%)'),
        ),
    ]
