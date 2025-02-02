# templatetags/custom_filters.py
from django import template
from datetime import date
import os
register = template.Library()

@register.filter(name='formatted_birth_date')
def formatted_birth_date(value):
    if isinstance(value, date):
        day = value.day
        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        return value.strftime(f"{day}{suffix} %B %Y")
    return value

@register.filter(name='formatted_start_end')
def formatted_start_end(value):
    if isinstance(value, date):
        return value.strftime("%d/%m/%Y")  # Formats the date as 'YYYY-MM-DD'
    return value

@register.filter(name='formate_year')
def formate_year(value):
    if isinstance(value, date):
        return value.strftime("%Y")  # Formats the date as 'YYYY-MM-DD'
    return value

@register.filter(name='replace_underscore')
def replace_underscore(value):
    if isinstance(value, str):
        return value.replace('_', ' ')
    return value

@register.filter
def basename(value):
    return os.path.basename(value)

@register.filter
def get_item(dictionary, key):
    """Custom filter to get an item from a dictionary."""
    return dictionary.get(key)

@register.filter
def get_skill_separated(skill_str):
    """Custom filter to get a list of skills separated by comma."""
    return skill_str.split(',') if skill_str else []