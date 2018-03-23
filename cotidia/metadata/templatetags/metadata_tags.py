from django import template
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from cotidia.metadata.models import MetaData

register = template.Library()


def append_domain(value):
    if value:
        if not value.url.startswith('http'):
            return settings.SITE_URL + value.url
        else:
            return value.url
    return None


@register.simple_tag
def get_meta_data(obj):
    try:
        metadata = MetaData.objects.get(
            object_id=obj.id,
            content_type=ContentType.objects.get_for_model(obj)
        )
        metadata.og_image_url = append_domain(metadata.og_image)
        metadata.twitter_image_src_url = append_domain(metadata.twitter_image_src)
        metadata.google_logo_url = append_domain(metadata.google_logo)
        metadata.url = settings.SITE_URL + obj.get_absolute_url()

        return metadata
    except MetaData.DoesNotExist:
        return None
