from django import template
from ..models import Madan

register = template.Library()


@register.inclusion_tag("madan/madan.html")
def nav():
    return {
        "madan": Madan.objects.all()
    }
