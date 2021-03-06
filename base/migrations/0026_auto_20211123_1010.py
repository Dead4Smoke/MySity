# Generated by Django 3.1.7 on 2021-11-23 07:10

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20211123_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablethree',
            name='PP3_1',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a1', 'Лучшая практика по комплексному подходу к предупреждению ЧС'), ('a2', 'Лучшая практика проведения профилактического мероприятия'), ('a3', 'Лучший культурно-просветительский проект'), ('a4', 'Лучшая практика привлечения дополнительного финансирования на снижение риска ЧС (практика взаимодействия с бизнесом)'), ('a5', 'Лучшая практика созданяи технологии, направленной на предупреждение ЧС')], max_length=14, null=True, verbose_name='Предупреждение ЧС'),
        ),
        migrations.AlterField(
            model_name='tablethree',
            name='PP3_2',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('b1', 'Лучшая практика проведения учения'), ('b2', 'Лучшая практика взаимодействия с население/детьми/молодежью/людьми с ограниченными возможностями здоровья'), ('b3', 'Лучшая практика по формированию компетенции по действиям в ЧС'), ('b4', 'Лучшая практика создания технологии, направленной на устойчивость в ЧС')], max_length=11, null=True, verbose_name='Готовность'),
        ),
        migrations.AlterField(
            model_name='tablethree',
            name='PP3_3',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('v1', ' Лучшая практика ликвидации/помощи в ликвидации ЧС природного характера '), ('v2', ' Лучшая практика ликвидации/помощи в ликвидации ЧС техногенного характера '), ('v3', ' Лучшая практика ликвидации/помощи в ликвидации пожаров '), ('v4', ' Лучшая практика организации первоочередного жизнеобеспечения населения '), ('v5', ' Лучшая практика создания технологии реагирования на ЧС ')], max_length=14, null=True, verbose_name='Реагирование'),
        ),
        migrations.AlterField(
            model_name='tablethree',
            name='PP3_4',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('g1', ' Лучшая практика взаимодействия с безнесом '), ('g2', ' Лучшая практика восстановления по принципу «лучше, чем было» ')], max_length=5, null=True, verbose_name='Восстановление'),
        ),
    ]
