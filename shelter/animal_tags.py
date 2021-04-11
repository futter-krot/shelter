from django import template
from sanctuary.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Animal.objects.all()
    else:
        return Animal.objects.filter(pk=filter)


