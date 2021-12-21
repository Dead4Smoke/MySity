from django import template
from django.template.defaultfilters import stringfilter
from base.models import registration

register = template.Library()

@register.filter
@stringfilter
def Sub(value):
    a = 'Заполните данные'
    autodok = registration.objects.filter(User=value).first()
    if autodok and autodok.Sub:
        return autodok.Sub
    else:
        return a  
register.filter('Sub', Sub)

@register.filter
@stringfilter
def Municipal(value):
    a = 'Заполните данные'
    autodok = registration.objects.filter(User=value).first()
    if autodok and autodok.Municipal:
        return autodok.Municipal
    else:
        return a
register.filter('Municipal', Municipal)

@register.filter
@stringfilter
def MunicipalHead(value):
    a = 'Заполните данные'
    autodok = registration.objects.filter(User=value).first()
    if autodok and autodok.MunicipalHead:
        return autodok.MunicipalHead
    else:
        return a
register.filter('MunicipalHead', MunicipalHead)