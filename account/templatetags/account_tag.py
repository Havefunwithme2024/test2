from django import template

register = template.Library()

@register.simple_tag()
def update_none(text):
    if text is None or text == 0:
        return 'Не указано'
    else:
        return text