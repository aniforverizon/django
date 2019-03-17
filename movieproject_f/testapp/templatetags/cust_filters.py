from django import template
register=template.Library()

@register.filter(name='flu')
def first_last_upper(value):
    result=value[0].upper()+value[1:len(value)-1].lower()+value[-1].upper()
    return result

@register.filter(name='f3')
def first_3_characters(value):
    return value[:3]

# register.filter('flu',first_last_upper)
