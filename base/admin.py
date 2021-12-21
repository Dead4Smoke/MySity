from django.contrib import admin
from .models import *

class registrationAdmin(admin.ModelAdmin):
    list_display = ('Sub','Municipal','MunicipalHead','AdminPost','WebSite','Area','Population','FIO','WorkPost','Number','Email','User')
admin.site.register(registration, registrationAdmin)

class TablezeroAdmin(admin.ModelAdmin):
    list_display = ('User',
            'ObjectA','ObjectB','ObjectC','ObjectD',
            'ObjectE','ObjectF','ObjectG','ObjectH',
            'ObjectI','ObjectJ','ObjectK','ObjectL',
            'ObjectM','ObjectN','ObjectO','ObjectP',
            'ObjectQ',)
admin.site.register(Tablezero, TablezeroAdmin)

class TableoneAdmin(admin.ModelAdmin):
    list_display = (
        'A1_1','A2_1','A3_1','A4_1','A5_1','A6_1','A7_1','A8_1','A9_1','A10_1',
        'A11_1','A12_1','A13_1','A14_1','A15_1','A16_1','A17_1','A18_1','A19_1','A20_1',
        'A1_2','A2_2','A3_2','A4_2','A5_2','A6_2','A7_2','A8_2','A9_2','A10_2',
        'A11_2','A12_2','A13_2','A14_2','A15_2','A16_2','A17_2','A18_2','A19_2','A20_2',
        'A1_3','A2_3','A3_3','A4_3','A5_3','A6_3','A7_3','A8_3','A9_3','A10_3',
        'A11_3','A12_3','A13_3','A14_3','A15_3','A16_3','A17_3','A18_3','A19_3','A20_3',
        'A1_4','A2_4','A3_4','A4_4','A5_4','A6_4','A7_4','A8_4','A9_4','A10_4',
        'A11_4','A12_4','A13_4','A14_4','A15_4','A16_4','A17_4','A18_4','A19_4','A20_4',
        'A1_5','A2_5','A3_5','A4_5','A5_5','A6_5','A7_5','A8_5','A9_5','A10_5',
        'A11_5','A12_5','A13_5','A14_5','A15_5','A16_5','A17_5','A18_5','A19_5','A20_5',
        'User')
admin.site.register(Tableone, TableoneAdmin)

class TabletwoAdmin(admin.ModelAdmin):
    list_display = ('qOh1','qTh1','qTTh1','qOh2','qTh2','qTTh2','qOh3','qTh3','qTTh3','qOh4','qTh4','qTTh4','qOh5','qTh5','qTTh5','qOh6','qTh6','qTTh6','User')
admin.site.register(Tabletwo, TabletwoAdmin)

class TablethreeAdmin(admin.ModelAdmin):
    list_display = ( 'PP1','PP2',
            'PP3_1','PP3_1_6',
            'PP3_2','PP3_2_5',
            'PP3_3','PP3_3_6',
            'PP3_4','PP3_4_3',
            'PP3_5',
            'PP4','PP5','PP6',
            'PP7','PP8',   
            'TT1','TT2','TT3','User',)
admin.site.register(Tablethree, TablethreeAdmin)

class regionAdmin(admin.ModelAdmin):
    list_display = (
        'region',
        )
admin.site.register(regionchoise, regionAdmin)

class cardAdmin(admin.ModelAdmin):
    list_display = (
                        'car1_1','car1_2','car1_3','car2_1','car2_2','car2_3','car2_4','car2_5','car3_1','car3_2','car3_3','car3_4','car4_1','car4_2','car4_3','car4_4','car5_1','car5_2','car5_3','car6_1','car6_2','car6_3','car6_4','car6_5','car6_6','car7_1','car7_2','car7_3','car7_4','car8_1','car8_2','car8_3','car8_4','car8_5','car8_6','car8_7','car8_8','car8_9','car9_1','car9_2','car9_3','car9_4','car9_5','car9_6','car9_7','car10_1','car10_2','User',
        )
admin.site.register(card, cardAdmin)


# Register your models here.
