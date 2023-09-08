from django import template

register = template.Library()

@register.filter(name="add_attr")
def add_attr(field, css):
    attrs = {}
    class_, value_ = css.split(':')
    attrs[class_] = value_
    return field.as_widget(attrs=attrs)
