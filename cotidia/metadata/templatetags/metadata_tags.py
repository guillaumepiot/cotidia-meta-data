from django import template
from django.conf import settings
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
    except MetaData.DoesNotExist:
        return None


def append_domain(value):
    if value:
        if not value.url.startswith('http'):
            return settings.SITE_URL + value.url
        else:
            return value.url
    return None


@register.inclusion_tag('metadata/metadata.html')
def print_meta_data(obj):
    metadata = get_meta_data(obj)

    if metadata:
        metadata.og_image_url = append_domain(metadata.og_image)
        metadata.twitter_image_src_url = append_domain(metadata.twitter_image_src)
        metadata.google_logo_url = append_domain(metadata.google_logo)
        metadata.url = settings.SITE_URL + obj.get_absolute_url()

        return {
            'metadata': metadata
        }
