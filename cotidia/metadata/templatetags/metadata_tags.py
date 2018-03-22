from django import template
from django.contrib.contenttypes.models import ContentType

from cotidia.metadata.models import MetaData

register = template.Library()


@register.simple_tag
def get_meta_data(obj):
    try:
        return MetaData.objects.get(
            object_id=obj.id,
            content_type=ContentType.objects.get_for_model(obj)
        )
    except MetaData.doesNotExist:
        return None

