from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    获取字典中的值
    用法: {{ dictionary|get_item:key }}
    """
    return dictionary.get(key) 