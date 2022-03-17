from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def wikilinks(value):
    re_link = re.compile(r"\[(.*?)\]")
    return mark_safe(re_link.sub(r"<a href='/\1/ '>\1</a>", value))