from docxtpl import DocxTemplate
from base.models import *
from datetime import date
from io import BytesIO


def get_Tabreg_doc(request):
   table1 = registration.objects.filter(User=request.user).first()
   if table1:
      table_objects = []
      table_objects.append({"name" : "Субъект Российской Федерации", "value": table1.Sub})
      table_objects.append({"name" : "Название муниципального образования", "value": table1.Municipal})
      table_objects.append({"name" : "ФИО Главы муниципального образования/ Главы местной администрации", "value": table1.MunicipalHead})
      table_objects.append({"name" : "Наименование должности главы муниципального образования/Главы местной администрации", "value": table1.AdminPost})
      table_objects.append({"name" : "Официальный веб сайт", "value": table1.WebSite})
      table_objects.append({"name" : "Площадь, кв.км", "value": table1.Area})
      table_objects.append({"name" : "Население, тыс. чел. (на момент заполнения заявки)", "value": table1.Population})
      table_objects.append({"name" : "ФИО должносного лица, ответственного за организационное сопровождение участие униципального образования в пилотном проэкте ", "value": table1.FIO})
      table_objects.append({"name" : "Должность ответственного лица", "value": table1.WorkPost})
      table_objects.append({"name" : "Телефон", "value": table1.Number})
      table_objects.append({"name" : "Почта", "value": table1.Email})
      doc = DocxTemplate("./base/static/base/dock/tab.docx")
      context = {
            "tbl1": table_objects
            }
      doc.render(context)
      b = BytesIO()
      doc.save(b)
      b.seek(0)
      return b
   return False

def get_Tab0_doc(request):
   table1 = Tablezero.objects.filter(User=request.user).first()
   a = table1.ObjectA
   b = table1.ObjectB
   c = table1.ObjectC
   d = table1.ObjectD
   e = table1.ObjectE
   f = table1.ObjectF
   g = table1.ObjectG
   h = table1.ObjectH
   i = table1.ObjectI
   j = table1.ObjectJ
   k = table1.ObjectK
   l = table1.ObjectL
   m = table1.ObjectM
   n = table1.ObjectN
   o = table1.ObjectO
   p = table1.ObjectP
   q = table1.ObjectQ
   doc = DocxTemplate("./base/static/base/dock/TAB0.docx")
   context = {
               'a': a,
               'b': b,
               'c': c,
               'd': d,
               'e': e,
               'f': f,
               'g': g,
               'h': h,
               'i': i,
               'j': j,
               'k': k,
               'l': l,
               'm': m,
               'n': n,
               'o': o,
               'p': p,
               'q': q,
             }
   doc.render(context)
   b = BytesIO()
   doc.save(b)
   b.seek(0)
   return b
 
def get_Tab1_doc(request):
   table1 = Tableone.objects.filter(User=request.user).first()
   a1_1 = table1.A1_1
   a2_1 = table1.A2_1
   a3_1 = table1.A3_1
   a4_1 = table1.A4_1
   a5_1 = table1.A5_1
   a6_1 = table1.A6_1
   a7_1 = table1.A7_1
   a8_1 = table1.A8_1
   a9_1 = table1.A9_1
   a10_1 = table1.A10_1
   a11_1 = table1.A11_1
   a12_1 = table1.A12_1
   a13_1 = table1.A13_1
   a14_1 = table1.A14_1
   a15_1 = table1.A15_1
   a16_1 = table1.A16_1
   a17_1 = table1.A17_1
   a18_1 = table1.A18_1
   a19_1 = table1.A19_1
   a20_1 = table1.A20_1
   a21_1 = table1.A21_1
   a1_2 = table1.A1_2
   a2_2 = table1.A2_2
   a3_2 = table1.A3_2
   a4_2 = table1.A4_2
   a5_2 = table1.A5_2
   a6_2 = table1.A6_2
   a7_2 = table1.A7_2
   a8_2 = table1.A8_2
   a9_2 = table1.A9_2
   a10_2 = table1.A10_2
   a11_2 = table1.A11_2
   a12_2 = table1.A12_2
   a13_2 = table1.A13_2
   a14_2 = table1.A14_2
   a15_2 = table1.A15_2
   a16_2 = table1.A16_2
   a17_2 = table1.A17_2
   a18_2 = table1.A18_2
   a19_2 = table1.A19_2
   a20_2 = table1.A20_2
   a21_2 = table1.A21_2
   a1_3 = table1.A1_3
   a2_3 = table1.A2_3
   a3_3 = table1.A3_3
   a4_3 = table1.A4_3
   a5_3 = table1.A5_3
   a6_3 = table1.A6_3
   a7_3 = table1.A7_3
   a8_3 = table1.A8_3
   a9_3 = table1.A9_3
   a10_3 = table1.A10_3
   a11_3 = table1.A11_3
   a12_3 = table1.A12_3
   a13_3 = table1.A13_3
   a14_3 = table1.A14_3
   a15_3 = table1.A15_3
   a16_3 = table1.A16_3
   a17_3 = table1.A17_3
   a18_3 = table1.A18_3
   a19_3 = table1.A19_3
   a20_3 = table1.A20_3
   a21_3 = table1.A21_3
   a1_4 = table1.A1_4
   a2_4 = table1.A2_4
   a3_4 = table1.A3_4
   a4_4 = table1.A4_4
   a5_4 = table1.A5_4
   a6_4 = table1.A6_4
   a7_4 = table1.A7_4
   a8_4 = table1.A8_4
   a9_4 = table1.A9_4
   a10_4 = table1.A10_4
   a11_4 = table1.A11_4
   a12_4 = table1.A12_4
   a13_4 = table1.A13_4
   a14_4 = table1.A14_4
   a15_4 = table1.A15_4
   a16_4 = table1.A16_4
   a17_4 = table1.A17_4
   a18_4 = table1.A18_4
   a19_4 = table1.A19_4
   a20_4 = table1.A20_4
   a21_4 = table1.A21_4
   a1_5 = table1.A1_5
   a2_5 = table1.A2_5
   a3_5 = table1.A3_5
   a4_5 = table1.A4_5
   a5_5 = table1.A5_5
   a6_5 = table1.A6_5
   a7_5 = table1.A7_5
   a8_5 = table1.A8_5
   a9_5 = table1.A9_5
   a10_5 = table1.A10_5
   a11_5 = table1.A11_5
   a12_5 = table1.A12_5
   a13_5 = table1.A13_5
   a14_5 = table1.A14_5
   a15_5 = table1.A15_5
   a16_5 = table1.A16_5
   a17_5 = table1.A17_5
   a18_5 = table1.A18_5
   a19_5 = table1.A19_5
   a20_5 = table1.A20_5
   a21_5 = table1.A21_5 
   doc = DocxTemplate("./base/static/base/dock/tab1.docx")
   context = {
         'a1_1': a1_1 ,
         'a2_1': a2_1 ,
         'a3_1': a3_1 ,
         'a4_1': a4_1 ,
         'a5_1': a5_1 ,
         'a6_1': a6_1 ,
         'a7_1': a7_1 ,
         'a8_1': a8_1 ,
         'a9_1': a9_1 ,
         'a10_1': a10_1 ,
         'a11_1': a11_1 ,
         'a12_1': a12_1 ,
         'a13_1': a13_1 ,
         'a14_1': a14_1 ,
         'a15_1': a15_1 ,
         'a16_1': a16_1 ,
         'a17_1': a17_1 ,
         'a18_1': a18_1 ,
         'a19_1': a19_1 ,
         'a20_1': a20_1 ,
         'a21_1': a21_1 ,
         'a1_2': a1_2 ,
         'a2_2': a2_2 ,
         'a3_2': a3_2 ,
         'a4_2': a4_2 ,
         'a5_2': a5_2 ,
         'a6_2': a6_2 ,
         'a7_2': a7_2 ,
         'a8_2': a8_2 ,
         'a9_2': a9_2 ,
         'a10_2': a10_2 ,
         'a11_2': a11_2 ,
         'a12_2': a12_2 ,
         'a13_2': a13_2 ,
         'a14_2': a14_2 ,
         'a15_2': a15_2 ,
         'a16_2': a16_2 ,
         'a17_2': a17_2 ,
         'a18_2': a18_2 ,
         'a19_2': a19_2 ,
         'a20_2': a20_2 ,
         'a21_2': a21_2 ,
         'a1_3': a1_3 ,
         'a2_3': a2_3 ,
         'a3_3': a3_3 ,
         'a4_3': a4_3 ,
         'a5_3': a5_3 ,
         'a6_3': a6_3 ,
         'a7_3': a7_3 ,
         'a8_3': a8_3 ,
         'a9_3': a9_3 ,
         'a10_3': a10_3 ,
         'a11_3': a11_3 ,
         'a12_3': a12_3 ,
         'a13_3': a13_3 ,
         'a14_3': a14_3 ,
         'a15_3': a15_3 ,
         'a16_3': a16_3 ,
         'a17_3': a17_3 ,
         'a18_3': a18_3 ,
         'a19_3': a19_3 ,
         'a20_3': a20_3 ,
         'a21_3': a21_3 ,
         'a1_4': a1_4 ,
         'a2_4': a2_4 ,
         'a3_4': a3_4 ,
         'a4_4': a4_4 ,
         'a5_4': a5_4 ,
         'a6_4': a6_4 ,
         'a7_4': a7_4 ,
         'a8_4': a8_4 ,
         'a9_4': a9_4 ,
         'a10_4': a10_4 ,
         'a11_4': a11_4 ,
         'a12_4': a12_4 ,
         'a13_4': a13_4 ,
         'a14_4': a14_4 ,
         'a15_4': a15_4 ,
         'a16_4': a16_4 ,
         'a17_4': a17_4 ,
         'a18_4': a18_4 ,
         'a19_4': a19_4 ,
         'a20_4': a20_4 ,
         'a21_4': a21_4 ,
         'a1_5': a1_5 ,
         'a2_5': a2_5 ,
         'a3_5': a3_5 ,
         'a4_5': a4_5 ,
         'a5_5': a5_5 ,
         'a6_5': a6_5 ,
         'a7_5': a7_5 ,
         'a8_5': a8_5 ,
         'a9_5': a9_5 ,
         'a10_5': a10_5 ,
         'a11_5': a11_5 ,
         'a12_5': a12_5 ,
         'a13_5': a13_5 ,
         'a14_5': a14_5 ,
         'a15_5': a15_5 ,
         'a16_5': a16_5 ,
         'a17_5': a17_5 ,
         'a18_5': a18_5 ,
         'a19_5': a19_5 ,
         'a20_5': a20_5 ,
         'a21_5': a21_5 , 
         }
   doc.render(context)
   b = BytesIO()
   doc.save(b)
   b.seek(0)
   return b
   
def get_Tab2_doc(request):
   table2 = Tabletwo.objects.filter(User=request.user).first()
   if table2:
      table_objects = [] 
      table_objects.append({"name" : "Да/Нет", "value": table2.qOh1})
      table_objects.append({"name" : "Обоснование", "value": table2.qTh1})
      table_objects.append({"name" : "Приложение", "value": table2.qTTh1})
      table_objects.append({"name" : "Да/Нет", "value": table2.qOh2})
      table_objects.append({"name" : "Обоснование", "value": table2.qTh2})
      table_objects.append({"name" : "Приложение", "value": table2.qTTh2})
      table_objects.append({"name" : "Да/Нет", "value": table2.qOh3})
      table_objects.append({"name" : "Обоснование", "value": table2.qTh3})
      table_objects.append({"name" : "Приложение", "value": table2.qTTh3})
      table_objects.append({"name" : "Да/Нет", "value": table2.qOh4})
      table_objects.append({"name" : "Обоснование", "value": table2.qTh4})
      table_objects.append({"name" : "Приложение", "value": table2.qTTh4})
      table_objects.append({"name" : "Да/Нет", "value": table2.qOh5})
      table_objects.append({"name" : "Обоснование", "value": table2.qTh5})
      table_objects.append({"name" : "Приложение", "value": table2.qTTh5})
      table_objects.append({"name" : "Да/Нет", "value": table2.qOh6})
      table_objects.append({"name" : "Обоснование", "value": table2.qTh6})
      table_objects.append({"name" : "Приложение", "value": table2.qTTh6})
      doc = DocxTemplate("./base/static/base/dock/tab2.docx")
      context = {
            "tbl1": table_objects
            }
      doc.render(context)
      b = BytesIO()
      doc.save(b)
      b.seek(0)
      return b
   return False

def get_Tab3_doc(request):
   table3 = Tablethree.objects.filter(User=request.user).first()
   if table3:
      table_objects = []
      table_objects.append({"name" : " ", "value": table3.PP1})
      table_objects.append({"name" : " ", "value": table3.PP2})
      table_objects.append({"name" : " ", "value": table3.PP3_1})
      table_objects.append({"name" : " ", "value": table3.PP3_1_6})
      table_objects.append({"name" : " ", "value": table3.PP3_2})   
      table_objects.append({"name" : " ", "value": table3.PP3_2_5})
      table_objects.append({"name" : " ", "value": table3.PP3_3})   
      table_objects.append({"name" : " ", "value": table3.PP3_3_6})
      table_objects.append({"name" : " ", "value": table3.PP3_4})
      table_objects.append({"name" : " ", "value": table3.PP3_4_3})
      table_objects.append({"name" : " ", "value": table3.PP3_5})
      table_objects.append({"name" : " ", "value": table3.PP4})
      table_objects.append({"name" : " ", "value": table3.PP5})
      table_objects.append({"name" : " ", "value": table3.PP6})
      table_objects.append({"name" : " ", "value": table3.PP7})
      table_objects.append({"name" : " ", "value": table3.PP8})
      table_objects.append({"name" : "Мероприятия, относящиеся к лучшим практикам, которыми город готов поделиться", "value": table3.TT1})
      table_objects.append({"name" : "Подтверждение(текст)", "value": table3.TT2})
      table_objects.append({"name" : "Подтверждение(фото)", "value": table3.TT3})
      doc = DocxTemplate("./base/static/base/dock/tab3.docx")
      context = {
            "tbl1": table_objects
            }
      doc.render(context)
      b = BytesIO()
      doc.save(b)
      b.seek(0)
      return b
   return False
