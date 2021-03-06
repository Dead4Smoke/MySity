# Generated by Django 3.1.7 on 2021-10-22 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='regionchoise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=200, unique=True, verbose_name='Введите регион')),
            ],
        ),
        migrations.CreateModel(
            name='Tablezero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ObjectA', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a1', 'Подтопление территории города;'), ('a2', 'Сейсмическая опасность, появление деформации земной поверхности в виде провалов и неравномерных оседаний земли;'), ('a3', 'Появление оползней;'), ('a4', 'Вероятность ураганов, штормового ветра, обильных снегопадов, и затяжных дождей, обледенение дорог и токонесущих проводов;'), ('a5', 'Падение крупных небесных тел(метеоритов, болидов);'), ('a6', 'Задымлление вследствие массовых торфяных и лесных пожаров;')], max_length=17, null=True, verbose_name='Типы угроза А:')),
                ('ObjectB', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('b1', 'Транспортные аварии, включая дорожно-транспортные происшествия, крушения поездов, железнодорожные аварии и авиационные катастрофы;'), ('b2', 'Пожары на промышленных объектах, транспорте и в жилых зданиях;'), ('b3', 'Обрушения элементов транспортных коммуникаций, производственных и непроизводственных зданий и сооружений;'), ('b4', 'Аварии на магистральных трубопроводах;'), ('b5', 'Аварии на подземных сооркжениях;'), ('b6', 'Прорывы гидротехнических сооружений, являющихся гидродинамически опасными объектами (плотин, запруд, дамб, шлюзов перемычек и др.) с образованием волн прорыва и катастрофических затоплений;'), ('b7', 'Аварии с выбросом химически опасных веществ и образованием зон химического заражения;'), ('b8', 'Аварии с выбросом радиоактивных веществ с образованием обширных зон загрязнения;'), ('b9', 'Аварии с разливом нефтепродуктов;'), ('b10', 'Аварии на электростанциях и сетях с долговременным перерывом электроснабжения основных потребителей;'), ('b11', 'Аварии на системах жизнеобеспечения и очистных сооружениях;'), ('b12', 'Прорывы в сетях тепло- и водоснабжения;'), ('b13', 'Старение жилого фонда, инженерной инфраструктуры;'), ('b14', 'Снижение надежности и устойчивости энергоснабжения;'), ('b15', 'Перегруженность магистральных инженерных сетей канализации и полей фильтрации;'), ('b16', 'Дефицит источников теплоснабжения;'), ('b17', 'Отсутствие технологий очистки питьевой воды;'), ('b18', 'Несвоевременная и некачественная уборка улиц;'), ('b19', 'Нарушение порядка утилизации производственных и бытовых отходов;'), ('b20', 'Воздействие внешних факторов на качество питьевой воды;'), ('b21', 'Несоответствие дорожного покрытия требованиям безопасности автомобильных перевозок;')], max_length=74, null=True, verbose_name='Типы угроза Б:')),
                ('ObjectV', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('c1', 'Массовые инфекционные и другие заболевания людей, связанные с социальной деятельностью людей;'), ('c2', 'Массовые инфекционные заболевания домашних животных, опасные болезни рыб;'), ('c3', 'Массовые поражения сельскохозяйственных растений болезнями и вредителями;')], max_length=8, null=True, verbose_name='Типы угроза В:')),
                ('ObjectG', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('d1', 'Просадки, оползни, обвалы земной поверхности из-за выработки недр при добыче полезных ископаемых и другой деятельности человека;'), ('d2', 'Наличие тяжелых металлов (в том числе радионуклидов) и других вредных веществ в почве(грунте) сверх предельно допустимых концентраций;'), ('d3', 'Интенсивная деградация почв, опустынивание на обширных территориях из-за эрозии, засоления, заболачивания почв и так далее;'), ('d4', 'Ситуации, связанные с истощением не возобновляемых природных ископаемых;'), ('d5', 'Ситуации, вызванные переполнением хранилищ (свалок) промышленными и бытовым отходами, загрязнением ими окружающей среды;'), ('d6', 'Резкие изменения погоды или климата в результате антропогенной деятельности;'), ('d7', 'Превышение предельно допустимой концентрации вредных примесей в атмосфере;'), ('d8', 'Температурные инверсии над городами;'), ('d9', '«Кислородный» голод в городах;'), ('d10', 'Значительное превышение предельно допустимого уровня городского шума;'), ('d11', 'Образование обширной зоны кислотных осадков;'), ('d12', 'Разрушение озонового слоя атмосферы;'), ('d13', 'Значительные изменения прозрачности атмосферы;'), ('d14', 'Недостаток питьевой воды вследствие истощения водных источников или их загрязнения;'), ('d15', 'Истощение водных ресурсов, необходимых для организации хозяйственно-бытового водоснабжения и обеспечения технологических процессов;'), ('d16', 'Нарушение хозяйственной деятельности и экологического равновесия вследствие загрязнения зон внутренних морей и мирового океана;')], max_length=54, null=True, verbose_name='Типы угроза Г:')),
                ('User', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Tabletwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qOh1', models.CharField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], max_length=10, null=True, verbose_name='Да/Нет')),
                ('qTh1', models.TextField(null=True, verbose_name='Обоснование')),
                ('qTTh1', models.FileField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Приложение')),
                ('qOh2', models.CharField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], max_length=10, null=True, verbose_name='Да/Нет')),
                ('qTh2', models.TextField(null=True, verbose_name='Обоснование')),
                ('qTTh2', models.FileField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Приложение')),
                ('qOh3', models.CharField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], max_length=10, null=True, verbose_name='Да/Нет')),
                ('qTh3', models.TextField(null=True, verbose_name='Обоснование')),
                ('qTTh3', models.FileField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Приложение')),
                ('qOh4', models.CharField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], max_length=10, null=True, verbose_name='Да/Нет')),
                ('qTh4', models.TextField(null=True, verbose_name='Обоснование')),
                ('qTTh4', models.FileField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Приложение')),
                ('qOh5', models.CharField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], max_length=10, null=True, verbose_name='Да/Нет')),
                ('qTh5', models.TextField(null=True, verbose_name='Обоснование')),
                ('qTTh5', models.FileField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Приложение')),
                ('qOh6', models.CharField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], max_length=10, null=True, verbose_name='Да/Нет')),
                ('qTh6', models.TextField(null=True, verbose_name='Обоснование')),
                ('qTTh6', models.FileField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Приложение')),
                ('User', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Tablethree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TT1', models.TextField(null=True, verbose_name='Мероприятия, относящиеся к лучшим практикам, которыми город готов поделиться')),
                ('TT2', models.TextField(null=True, verbose_name='Подтверждение(текст)')),
                ('TT3', models.FileField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Подтверждение(фото)')),
                ('User', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Tableone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A1_2016', models.IntegerField(null=True, verbose_name='Численность постоянного населения на 1 января текущего года (тыс. чел.)')),
                ('A2_2016', models.IntegerField(null=True, verbose_name='Количество лечебно-профилактической организации (ед.)')),
                ('A3_2016', models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных дошкольных образовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)')),
                ('A4_2016', models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных общеобразовательных организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)')),
                ('A5_2016', models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Доля муниципальных учереждений культуры организаций, здания которых находяться в аварийном состоянии, или требуют капитального ремонта, в общем числе муниципальных дошкольных образовательных организаций (%)')),
                ('A6_2016', models.IntegerField(null=True, verbose_name='Численность населения, охваченного системами оповещения (тыс.чел %) от общей численности населения территории')),
                ('A7_2016', models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Наличие утвержденного документа территориальногшо планирования')),
                ('A8_2016', models.IntegerField(blank=True, choices=[('y', 'Да'), ('n', 'Нет')], null=True, verbose_name='Наличие документа градостроительного зонирования ')),
                ('A9_2016', models.IntegerField(blank=True, choices=[(0, 0), (25, 25), (50, 50), (75, 75), (100, 100)], null=True, verbose_name='Степень износа жилого фонда (%)')),
                ('A10_2016', models.IntegerField(null=True, verbose_name='Смертность населения трудоспособного возраста (чел.)')),
                ('A11_2016', models.IntegerField(null=True, verbose_name='Смертность от ДТП (чел.)')),
                ('A12_2016', models.IntegerField(null=True, verbose_name='Количество погибших при авариях и происшествиях (чел.)')),
                ('A13_2016', models.IntegerField(null=True, verbose_name='Количество населения, погибшего в чрезвычайных ситуациях (чел.)')),
                ('A14_2016', models.IntegerField(null=True, verbose_name='Количество людей, погибших в результате пожара (чел.)')),
                ('A15_2016', models.IntegerField(null=True, verbose_name='Количество погибших в происшествиях на водных объектах ')),
                ('A16_2016', models.IntegerField(null=True, verbose_name='Количество населения, пострадавшего в чрезвычайных ситуациях (чел.)')),
                ('A17_2016', models.IntegerField(null=True, verbose_name='Количество людей, травмированных в результате пожаров (чел.)')),
                ('A18_2016', models.IntegerField(null=True, verbose_name='Количество ЧС природного характера, в которых погибло 10 и более человек')),
                ('A19_2016', models.IntegerField(null=True, verbose_name='Количество ЧС техногенного характера, в которых погибло 10 и более человек')),
                ('A20_2016', models.IntegerField(null=True, verbose_name='Количество пожаров, в которых погибло 10 и более человек')),
                ('User', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Municipal', models.TextField(null=True, verbose_name='Название муниципального образования')),
                ('MunicipalHead', models.TextField(null=True, verbose_name='ФИО Главы муниципального образования/ Главы местной администрации')),
                ('AdminPost', models.TextField(null=True, verbose_name='Наименование должности главы муниципального образования/Главы местной администрации')),
                ('WebSite', models.URLField(null=True, verbose_name='Веб сайт')),
                ('Area', models.TextField(null=True, verbose_name='Площадь, кв.км')),
                ('Population', models.TextField(null=True, verbose_name='Население, тыс. чел.')),
                ('FIO', models.TextField(null=True, verbose_name='ФИО должносного лица, ответственного за организационное сопровождение участие униципального образования в конкурсе')),
                ('WorkPost', models.TextField(null=True, verbose_name='Должность ответственного лица')),
                ('Number', models.IntegerField(null=True, verbose_name='Телефон')),
                ('Email', models.EmailField(max_length=254, null=True, verbose_name='Почта')),
                ('Sub', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.regionchoise', verbose_name='Субъект Российской Федерации')),
                ('User', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='calculate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.FloatField(null=True, verbose_name='q1')),
                ('q2', models.FloatField(null=True, verbose_name='q2')),
                ('q3', models.FloatField(null=True, verbose_name='q3')),
                ('q4', models.FloatField(null=True, verbose_name='q4')),
                ('q5', models.FloatField(null=True, verbose_name='q5')),
                ('q6', models.FloatField(null=True, verbose_name='q6')),
                ('q7', models.FloatField(null=True, verbose_name='q7')),
                ('q8', models.FloatField(null=True, verbose_name='q8')),
                ('Gk', models.FloatField(null=True, verbose_name='Gk')),
                ('Vk', models.FloatField(null=True, verbose_name='Vk')),
                ('Uk', models.FloatField(null=True, verbose_name='Uk')),
                ('Ik', models.FloatField(null=True, verbose_name='Ik')),
                ('User', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
