from django import template
from django.utils.timesince import timesince
from django.utils.timezone import is_aware, make_aware, get_current_timezone
from datetime import datetime

register = template.Library()

@register.filter
def custom_timesince(value):
    now = datetime.now()
    if is_aware(value):
        now = make_aware(now, get_current_timezone())
    time_diff = timesince(value, now)
    time_units = time_diff.split(', ')
    return time_units[0] + ' ago'