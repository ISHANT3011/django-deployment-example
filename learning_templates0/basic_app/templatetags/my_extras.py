from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cut out all arg values from the string
    """
    return value.replace(arg,'')

##register.filter('cut',cut)
