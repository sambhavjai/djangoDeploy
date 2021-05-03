from django import template

register = template.Library()

@register.filter(name='sam') #Use of a decorator in python
def sam(value,args):
    return value.replace(args,'')
