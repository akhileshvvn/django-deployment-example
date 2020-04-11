from django import template

register = template.library()


@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts all values of arg from string!
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')


#register.filter('cut',cut)