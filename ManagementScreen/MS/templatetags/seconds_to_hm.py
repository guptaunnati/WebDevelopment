from django import template

register = template.Library()

@register.simple_tag
def seconds_to_hm(seconds):
    if seconds == '':
        return ''
    seconds = int(seconds)
    days = seconds // (24 * 3600)
    hours = (seconds % (24 * 3600)) // 3600
    minutes = (seconds % 3600) // 60
    
    if seconds >=86400:
         return f"{str(days).zfill(2)}:{str(hours).zfill(2)}"
    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}"
