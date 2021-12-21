from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from base.templatetags.wordTab1 import *
from django.views.generic import ListView


@login_required
def office(request):
    autodok = registration.objects.filter(User=request.user).first()
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                old_form = registration.objects.get(User=request.user)
                old_form.delete()
            except registration.DoesNotExist as e:
                pass
            ###New
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            ###
            messages.success(request, 'Ваши данные отправлены на проверку')
            return redirect('office')         
        else:
            messages.success(request, 'Заполните поля правильно!')
    form = RegistrationForm(instance=autodok)
    is_exist = False
    try:
        registration.objects.get(User=request.user)
        is_exist = True
    except:
        pass     
    data = {
        'form' : form,
        'error': error,
        'is_exist': is_exist,
        }
    return render(request, 'base/office.html', data)

@login_required
def tab0(request):
    autodok = Tablezero.objects.filter(User=request.user).first()
    error = ''
    if request.method == 'POST':
            #Сохранение с пользователем
        #post_data = request.body.decode('utf-8').split("&")
            ###
        form = TablezeroForm(request.POST)
        if form.is_valid():
            try:
                old_form = Tablezero.objects.get(User=request.user)
                old_form.delete()
            except Tablezero.DoesNotExist as e:
                pass
            ###New
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            ###
            messages.success(request, 'Ваши данные отправлены на проверку')
            return redirect('tab0')
        else:
            messages.success(request, 'Заполните поля правильно!')
    form = TablezeroForm(instance=autodok)
    is_exist = False
    try:
        Tablezero.objects.get(User=request.user)
        is_exist = True
    except:
        pass     
    data = {
        'form' : form,
        'error': error,
        'is_exist': is_exist,
        }
    return render(request, 'base/tab0.html', data)

@login_required       
def tab1(request):
    autodok = Tableone.objects.filter(User=request.user).first()
    error = ''
    if request.method == 'POST':
        form = TableoneForm(request.POST)
        if form.is_valid():
            try:  
                old_form = Tableone.objects.get(User=request.user)
                old_form.delete()               
            except Tableone.DoesNotExist as e:
                pass
            ###New
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            ###
            messages.success(request, 'Ваши данные отправлены на проверку')
            return redirect('tab1')
        else:
            messages.success(request, 'Заполните поля правильно!')           
    form = TableoneForm(instance=autodok)
    is_exist = False
    try:
        Tableone.objects.get(User=request.user)
        is_exist = True
    except:
        pass        
    data = {
        'form' : form,
        'error': error,
        'is_exist': is_exist
        }
    return render(request, 'base/tab1.html', data)

@login_required   
def tab2(request):
    autodok = Tabletwo.objects.filter(User=request.user).first()
    error = ''
    if request.method == 'POST':
        form = TabletwoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                old_form = Tabletwo.objects.get(User=request.user)
                old_form.delete()
            except Tabletwo.DoesNotExist as e:
                pass
            ###New
            # newdoc = Tabletwo(qTTh1 = request.POST['qTTh1'])
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            ###
            messages.success(request, 'Ваши данные отправлены на проверку')
            return redirect('tab2')
        else:
            messages.success(request, 'Заполните поля правильно!')
            
    form = TabletwoForm(instance=autodok)
    is_exist = False
    try:
        Tabletwo.objects.get(User=request.user)
        is_exist = True
    except:
        pass
    data = {
        'form' : form,
        'error': error,
        'is_exist': is_exist
        }
    return render(request, 'base/tab2.html', data)

@login_required
def tab3(request):
    autodok = Tablethree.objects.filter(User=request.user).first()
    error = ''
    if request.method == 'POST':
            #Сохранение с пользователем
        #post_data = request.body.decode('utf-8').split("&")
            ###    
        form = TableThreeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                old_form = Tablethree.objects.get(User=request.user)
                old_form.delete()
            except Tablethree.DoesNotExist as e:
                pass
            ###New  
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            ###
            messages.success(request, 'Ваши данные отправлены на проверку')
            return redirect('tab3')
        else:
            messages.success(request, 'Заполните поля правильно!')
    form = TableThreeForm(instance=autodok)
    is_exist = False
    try:
        Tablethree.objects.get(User=request.user)
        is_exist = True 
    except:
        pass
    data = {
        'form' : form,
        'error': error,
        'is_exist': is_exist,
        }
    return render(request, 'base/tab3.html', data)

@login_required
def downloadtabreg(request):
    doc = get_Tabreg_doc(request)
    if doc:
        print(doc)
        response = HttpResponse(doc.read(), content_type="application/word")
        response['Content-Disposition'] = 'inline; filename=application.docx'
        return response
    else:
        raise Http404

@login_required
def downloadtab0(request):
    doc = get_Tab0_doc(request)
    if doc:
        response = HttpResponse(doc.read(), content_type="application/word")
        response['Content-Disposition'] = 'inline; filename=sources of emergency.docx'
        return response
    else:
        raise Http404

@login_required
def downloadtab1(request):
    doc = get_Tab1_doc(request)
    if doc:
        response = HttpResponse(doc.read(), content_type="application/word")
        response['Content-Disposition'] = 'inline; filename=statistical data.docx'
        return response
    else:
        raise Http404

@login_required
def downloadtab2(request):
    doc = get_Tab2_doc(request)
    if doc:
        response = HttpResponse(doc.read(), content_type="application/word")
        response['Content-Disposition'] = 'inline; filename=project passport.docx'
        return response
    else:
        raise Http404

@login_required
def downloadtab3(request):
    doc = get_Tab3_doc(request)
    if doc:
        response = HttpResponse(doc.read(), content_type="application/word")
        response['Content-Disposition'] = 'inline; filename=scorecard.docx'
        return response
    else:
        raise Http404 

class SearchResultsView(ListView):
    model = Tableone
    template_name = 'base/search.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('Sub')
        users = registration.objects.filter(Sub=query)
        tables = []
        for user in users:
            reg = registration.objects.filter(User=user.User).first()
            table = Tableone.objects.filter(User=user.User).first() 
            table2 = Tablethree.objects.filter(User=user.User).first()    
            table3 = Tablethree.objects.filter(User=user.User).first()
            cards = card.objects.filter(User=user.User).first()
            table.registration = user

            # данные из личного кабинета
            table.Sub = reg.Sub
            table.Municipal = reg.Municipal
            table.MunicipalHead = reg.MunicipalHead
            table.AdminPost = reg.AdminPost
            table.WebSite = reg.WebSite
            table.Area = reg.Area
            table.Population = reg.Population
            table.FIO = reg.FIO
            table.WorkPost = reg.WorkPost
            table.Number = reg.Number
            table.Email = reg.Email

            # данные из паспорта проэкта
            table.PP1 = table3.PP1
            table.PP2 = table3.PP2
            table.PP3_1 = table3.PP3_1
            table.PP3_1_6 = table3.PP3_1_6
            table.PP3_2 = table3.PP3_2
            table.PP3_2_5 = table3.PP3_2_5
            table.PP3_3 = table3.PP3_3
            table.PP3_3_6 = table3.PP3_3_6
            table.PP3_4 = table3.PP3_4       
            table.PP3_4_3 = table3.PP3_4_3
            table.PP3_5 = table3.PP3_5
            table.PP4 = table3.PP4
            table.PP5 = table3.PP5
            table.PP6 = table3.PP6
            table.PP7 = table3.PP7
            table.PP8 = table3.PP8
            table.TT1 = table3.TT1
            table.TT2 = table3.TT2
            table.TT3 = table3.TT3 

             # данные из оценочной карты
            table.car1_1 = cards.car1_1
            table.car1_2 = cards.car1_2 
            table.car1_3 = cards.car1_3

            table.car2_1 = cards.car2_1  
            table.car2_2 = cards.car2_2 
            table.car2_3 = cards.car2_3 
            table.car2_4 = cards.car2_4 
            table.car2_5 = cards.car2_5

            table.car3_1 = cards.car3_1 
            table.car3_2 = cards.car3_2 
            table.car3_3 = cards.car3_3
            table.car3_4 = cards.car3_4

            table.car4_1 = cards.car4_1 
            table.car4_2 = cards.car4_2 
            table.car4_3 = cards.car4_3
            table.car4_4 = cards.car4_4

            table.car5_1 = cards.car5_1
            table.car5_2 = cards.car5_2 
            table.car5_3 = cards.car5_3

            table.car6_1 = cards.car6_1 
            table.car6_2 = cards.car6_2 
            table.car6_3 = cards.car6_3
            table.car6_4 = cards.car6_4
            table.car6_5 = cards.car6_5
            table.car6_6 = cards.car6_6

            table.car7_1 = cards.car7_1 
            table.car7_2 = cards.car7_2 
            table.car7_3 = cards.car7_3
            table.car7_4 = cards.car7_4

            table.car8_1 = cards.car8_1 
            table.car8_2 = cards.car8_2 
            table.car8_3 = cards.car8_3
            table.car8_4 = cards.car8_4
            table.car8_5 = cards.car8_5
            table.car8_6 = cards.car8_6
            table.car8_7 = cards.car8_7
            table.car8_8 = cards.car8_8
            table.car8_9 = cards.car8_9

            table.car9_1 = cards.car9_1 
            table.car9_2 = cards.car9_2 
            table.car9_3 = cards.car9_3
            table.car9_4 = cards.car9_4
            table.car9_5 = cards.car9_5
            table.car9_6 = cards.car9_6
            table.car9_7 = cards.car9_7

            table.car10_1 = cards.car10_1 
            table.car10_2 = cards.car10_2 

            tables.append(table)
        return tables



@login_required
def region(request):
    table = Tableone.objects.all()
    form = RegistrationForm(request.POST)
    region = {
        'table': table,
        'form': form,
    }
    return render(request, 'base/region.html', { 'region': region })                        

@login_required
def cards(request):
    autodok = card.objects.filter(User=request.user).first()
    error = ''
    if request.method == 'POST':
        form = cardForm(request.POST)
        if form.is_valid():
            try:  
                old_form = card.objects.get(User=request.user)
                old_form.delete()
               
            except card.DoesNotExist as e:
                pass
            ###New
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            ###
            messages.success(request, 'Ваши данные отправлены на проверку')
            return redirect('card')
        else:
            messages.success(request, 'Заполните поля правильно!')
            
    form = cardForm(instance=autodok)
    is_exist = False
    try:
        card.objects.get(User=request.user)
        is_exist = True
    except:
        pass        
    data = {
        'form' : form,
        'error': error,
        'is_exist': is_exist
        }
    return render(request, 'base/card.html', data)   

@login_required
def statistical(request):
    stat = Tableone.objects.filter(User=request.user).first()
    data = {
        'stat': stat,
    }
    return render(request, 'base/statistical.html', data) 