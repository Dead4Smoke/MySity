from django.forms import widgets
from django.forms.widgets import CheckboxSelectMultiple, FileInput, Textarea
from .models import *
from django.forms import ModelForm, TextInput, Select

class RegistrationForm(ModelForm):
    class Meta:
        model = registration
        fields = [ 'Sub','Municipal','MunicipalHead','AdminPost','WebSite','Area','Population','FIO','WorkPost','Number','Email','User',]
        widgets = {  
            "Sub": Select(attrs={'class': 'form-control bor','type': 'text',}),
            "Municipal": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "MunicipalHead": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "AdminPost": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "WebSite": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "Area": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "Population": TextInput(attrs={'class': 'form-control bor','type': 'text',}),        
            "FIO": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "WorkPost": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "Number": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "Email": TextInput(attrs={'class': 'form-control bor','type': 'text',}),
            "User": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

        }

class TablezeroForm(ModelForm):
    class Meta:
        model = Tablezero
        fields = [
            'User',
            'ObjectA','ObjectB','ObjectC','ObjectD',
            'ObjectE','ObjectF','ObjectG','ObjectH',
            'ObjectI','ObjectJ','ObjectK','ObjectL',
            'ObjectM','ObjectN','ObjectO','ObjectP',
            'ObjectQ',]
        widgets = {  
            "User": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "ObjectA": CheckboxSelectMultiple(),
            "ObjectB": CheckboxSelectMultiple(),
            "ObjectC": CheckboxSelectMultiple(),
            "ObjectD": CheckboxSelectMultiple(),
            "ObjectE": CheckboxSelectMultiple(),
            "ObjectF": CheckboxSelectMultiple(),
            "ObjectG": CheckboxSelectMultiple(),
            "ObjectH": CheckboxSelectMultiple(),
            "ObjectI": CheckboxSelectMultiple(),
            "ObjectJ": CheckboxSelectMultiple(),
            "ObjectK": CheckboxSelectMultiple(),
            "ObjectL": CheckboxSelectMultiple(),
            "ObjectM": CheckboxSelectMultiple(),
            "ObjectN": CheckboxSelectMultiple(),
            "ObjectO": CheckboxSelectMultiple(),
            "ObjectP": CheckboxSelectMultiple(),
            "ObjectQ": CheckboxSelectMultiple(),
        }

class TableoneForm(ModelForm):
    class Meta:
        model = Tableone
        fields = [
            'A1_1','A2_1','A3_1','A4_1','A5_1','A6_1','A7_1','A8_1','A9_1','A10_1',
            'A11_1','A12_1','A13_1','A14_1','A15_1','A16_1','A17_1','A18_1','A19_1','A20_1','A21_1',

            'A1_2','A2_2','A3_2','A4_2','A5_2','A6_2','A7_2','A8_2','A9_2','A10_2',
            'A11_2','A12_2','A13_2','A14_2','A15_2','A16_2','A17_2','A18_2','A19_2','A20_2','A21_2',

            'A1_3','A2_3','A3_3','A4_3','A5_3','A6_3','A7_3','A8_3','A9_3','A10_3',
            'A11_3','A12_3','A13_3','A14_3','A15_3','A16_3','A17_3','A18_3','A19_3','A20_3','A21_3',

            'A1_4','A2_4','A3_4','A4_4','A5_4','A6_4','A7_4','A8_4','A9_4','A10_4',
            'A11_4','A12_4','A13_4','A14_4','A15_4','A16_4','A17_4','A18_4','A19_4','A20_4','A21_4',

            'A1_5','A2_5','A3_5','A4_5','A5_5','A6_5','A7_5','A8_5','A9_5','A10_5',
            'A11_5','A12_5','A13_5','A14_5','A15_5','A16_5','A17_5','A18_5','A19_5','A20_5','A21_5',

            'User'
            ]
        widgets = {  
            "A1_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A2_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A3_1": Select(attrs={'class': 'form-control','type': 'text',}),
            "A4_1": Select(attrs={'class': 'form-control','type': 'text',}),
            "A5_1": Select(attrs={'class': 'form-control','type': 'text',}),
            "A6_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A7_1": Select(attrs={'class': 'form-control','type': 'text',}),
            "A8_1": Select(attrs={'class': 'form-control','type': 'text',}),
            "A9_1": Select(attrs={'class': 'form-control','type': 'text',}),
            "A10_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A11_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A12_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A13_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A14_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A15_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A16_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A17_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A18_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A19_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A20_1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A21_1": TextInput(attrs={'class': 'form-control','type': 'text',}),

            "A1_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A2_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A3_2": Select(attrs={'class': 'form-control','type': 'text',}),
            "A4_2": Select(attrs={'class': 'form-control','type': 'text',}),
            "A5_2": Select(attrs={'class': 'form-control','type': 'text',}),
            "A6_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A7_2": Select(attrs={'class': 'form-control','type': 'text',}),
            "A8_2": Select(attrs={'class': 'form-control','type': 'text',}),
            "A9_2": Select(attrs={'class': 'form-control','type': 'text',}),
            "A10_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A11_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A12_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A13_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A14_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A15_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A16_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A17_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A18_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A19_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A20_2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A21_2": TextInput(attrs={'class': 'form-control','type': 'text',}),

            "A1_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A2_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A3_3": Select(attrs={'class': 'form-control','type': 'text',}),
            "A4_3": Select(attrs={'class': 'form-control','type': 'text',}),
            "A5_3": Select(attrs={'class': 'form-control','type': 'text',}),
            "A6_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A7_3": Select(attrs={'class': 'form-control','type': 'text',}),
            "A8_3": Select(attrs={'class': 'form-control','type': 'text',}),
            "A9_3": Select(attrs={'class': 'form-control','type': 'text',}),
            "A10_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A11_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A12_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A13_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A14_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A15_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A16_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A17_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A18_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A19_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A20_3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A21_3": TextInput(attrs={'class': 'form-control','type': 'text',}),

            "A1_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A2_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A3_4": Select(attrs={'class': 'form-control','type': 'text',}),
            "A4_4": Select(attrs={'class': 'form-control','type': 'text',}),
            "A5_4": Select(attrs={'class': 'form-control','type': 'text',}),
            "A6_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A7_4": Select(attrs={'class': 'form-control','type': 'text',}),
            "A8_4": Select(attrs={'class': 'form-control','type': 'text',}),
            "A9_4": Select(attrs={'class': 'form-control','type': 'text',}),
            "A10_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A11_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A12_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A13_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A14_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A15_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A16_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A17_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A18_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A19_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A20_4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A21_4": TextInput(attrs={'class': 'form-control','type': 'text',}),

            "A1_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A2_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A3_5": Select(attrs={'class': 'form-control','type': 'text',}),
            "A4_5": Select(attrs={'class': 'form-control','type': 'text',}),
            "A5_5": Select(attrs={'class': 'form-control','type': 'text',}),
            "A6_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A7_5": Select(attrs={'class': 'form-control','type': 'text',}),
            "A8_5": Select(attrs={'class': 'form-control','type': 'text',}),
            "A9_5": Select(attrs={'class': 'form-control','type': 'text',}),
            "A10_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A11_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A12_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A13_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A14_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A15_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A16_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A17_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A18_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A19_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A20_5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A21_5": TextInput(attrs={'class': 'form-control','type': 'text',}),

            
            "User": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
        }

class TabletwoForm(ModelForm):
    class Meta:
        model = Tabletwo
        fields = ['qOh1','qTh1','qTTh1','qOh2','qTh2','qTTh2','qOh3','qTh3','qTTh3','qOh4','qTh4','qTTh4','qOh5','qTh5','qTTh5','qOh6','qTh6','qTTh6','User']
        widgets = {  
            "qOh1": Select(attrs={'class': 'form-control bor bor2','type': 'text',}),
            "qTh1": Textarea(attrs={'class': 'form-control bor tab2','placeholder':'Обоснование'}),
            "qTTh1": FileInput(attrs={'class': 'form-control bor bor2'}),         
            "qOh2": Select(attrs={'class': 'form-control bor bor2','type': 'text',}),
            "qTh2": Textarea(attrs={'class': 'form-control bor tab2','placeholder':'Обоснование'}),
            "qTTh2": FileInput(attrs={'class': 'form-control bor bor2'}),
            "qOh3": Select(attrs={'class': 'form-control bor bor2','type': 'text',}),
            "qTh3": Textarea(attrs={'class': 'form-control bor tab2','placeholder':'Обоснование'}),
            "qTTh3": FileInput(attrs={'class': 'form-control bor bor2'}),
            "qOh4": Select(attrs={'class': 'form-control bor bor2','type': 'text',}),
            "qTh4": Textarea(attrs={'class': 'form-control bor tab2','placeholder':'Обоснование'}),
            "qTTh4": FileInput(attrs={'class': 'form-control bor bor2'}),
            "qOh5": Select(attrs={'class': 'form-control bor bor2','type': 'text',}),
            "qTh5": Textarea(attrs={'class': 'form-control bor tab2', 'placeholder':'Обоснование'}),
            "qTTh5": FileInput(attrs={'class': 'form-control bor bor2'}),
            "qOh6": Select(attrs={'class': 'form-control bor bor2','type': 'text',}),
            "qTh6": Textarea(attrs={'class': 'form-control bor tab2', 'placeholder':'Обоснование'}),
            "qTTh6": FileInput(attrs={'class': 'form-control bor bor2'}),
            "User": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
        }

class TableThreeForm(ModelForm):
    class Meta:
        model = Tablethree
        fields = [
            'PP1','PP2',
            'PP3_1','PP3_1_6',
            'PP3_2','PP3_2_5',
            'PP3_3','PP3_3_6',
            'PP3_4','PP3_4_3',
            'PP3_5',
            'PP4','PP5','PP6',
            'PP7','PP8',   
            'TT1','TT2','TT3','User',
            ]

        widgets = {  
            "PP1": Textarea(attrs={'class': 'form-control bor bortab3',}),
            "PP2": Textarea(attrs={'class': 'form-control bor bortab3',}),

            "PP3_1":    CheckboxSelectMultiple(),
            "PP3_1_6":  Textarea(attrs={'class': 'form-control bor bortab33',}),

            "PP3_2":    CheckboxSelectMultiple(),
            "PP3_2_5":  Textarea(attrs={'class': 'form-control bor bortab33',}),

            "PP3_3_1":  CheckboxSelectMultiple(), 
            "PP3_3_6":  Textarea(attrs={'class': 'form-control bor bortab33',}),

            "PP3_4_1":  CheckboxSelectMultiple(),         
            "PP3_4_3":  Textarea(attrs={'class': 'form-control bor bortab33',}),

            "PP3_5":    Textarea(attrs={'class': 'form-control bor bortab33',}),

            "PP4": Textarea(attrs={'class': 'form-control bor bortab3',}),      
            "PP5": Textarea(attrs={'class': 'form-control bor bortab3',}),
            "PP6": Textarea(attrs={'class': 'form-control bor bortab3',}),
            "PP7": Textarea(attrs={'class': 'form-control bor bortab3',}),
            "PP8": Textarea(attrs={'class': 'form-control bor bortab3',}),
            "TT1": Textarea(attrs={'class': 'form-control bor bortab3',}),
            "TT2": Textarea(attrs={'class': 'form-control bor bortab3',}),
            "TT3": FileInput(attrs={'class': 'form-control bor bor2'}),
            "User": Select(attrs={'class': 'form-control2 bor','type': 'text',}),      
        }

class cardForm(ModelForm):
    class Meta:
        model = card
        fields =    [
                        'car1_1','car1_2','car1_3',
                        'car2_1','car2_2','car2_3','car2_4','car2_5',
                        'car3_1','car3_2','car3_3','car3_4',
                        'car4_1','car4_2','car4_3','car4_4',
                        'car5_1','car5_2','car5_3',
                        'car6_1','car6_2','car6_3','car6_4','car6_5','car6_6',
                        'car7_1','car7_2','car7_3','car7_4',
                        'car8_1','car8_2','car8_3','car8_4','car8_5','car8_6','car8_7','car8_8','car8_9',
                        'car9_1','car9_2','car9_3','car9_4','car9_5','car9_6','car9_7',
                        'car10_1','car10_2',                    
                        'User'
        ]
        widgets =   {
            "User": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

            "car1_1": Select(attrs={'class': ' select-css','type': 'text',}),
            "car1_2": Select(attrs={'class': 'form-control2 bor select-css','type': 'text',}),
            "car1_3": Select(attrs={'class': 'form-control2 bor select-css','type': 'text',}),

            "car2_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car2_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car2_3": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car2_4": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car2_5": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

            "car3_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car3_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car3_3": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car3_4": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            
            "car4_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car4_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car4_3": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car4_4": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

            "car5_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car5_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car5_3": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

            "car6_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car6_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car6_3": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car6_4": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car6_5": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car6_6": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

            "car7_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car7_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car7_3": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car7_4": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

            "car8_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car8_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car8_3": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car8_4": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car8_5": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car8_6": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car8_7": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car8_8": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car8_9": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

            "car9_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car9_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car9_3": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car9_4": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car9_5": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car9_6": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car9_7": Select(attrs={'class': 'form-control2 bor','type': 'text',}),

            "car10_1": Select(attrs={'class': 'form-control2 bor','type': 'text',}),
            "car10_2": Select(attrs={'class': 'form-control2 bor','type': 'text',}),          
        }           
