from django import template

from cotidia.metadata.models import MetaData, Department

register = template.Library()


@register.simple_tag
def get_departments():
    return Department.objects.all().order_by('order_id')


@register.simple_tag
def get_members():
    return MetaData.objects.filter(active=True).order_by('order_id')
