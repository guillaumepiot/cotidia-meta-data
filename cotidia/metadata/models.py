from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from cotidia.core.models import BaseModel
from cotidia.admin.models import AbstractOrderable
from cotidia.core.fields import PublicFileField


class MetaData(AbstractOrderable, BaseModel):

    OG_TYPES = (
        ('article', 'article'),
        ('book', 'book'),
        ('profile', 'profile'),
        ('website', 'website'),
    )

    TWITTER_CARD_TYPES = (
        ('summary_large_image', 'summary large image'),
        ('app', 'app'),
        ('player', 'player'),
    )

    GOOGLE_TYPES = (
        ('Person', 'Person'),
        ('Organization', 'Organization'),
        ('WebSite', 'WebSite'),
        ('NewsArticle', 'NewsArticle'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # SEO
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(max_length=500, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)

    # Open Graph
    og_type = models.CharField(max_length=50, choices=OG_TYPES, null=True, blank=True)
    og_title = models.CharField(max_length=50, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_image = PublicFileField(upload_to='metadata', null=True, blank=True, help_text='Recommended size: 1200 x 630 px')

    # Twitter card
    twitter_card = models.CharField(max_length=50, choices=TWITTER_CARD_TYPES, help_text='Type of Twitter card')
    twitter_site = models.CharField(max_length=50, help_text='Twitter handle. E.g. @cotidia', null=True, blank=True)
    twitter_title = models.CharField(max_length=50, help_text='Title of the card', null=True, blank=True)
    twitter_description = models.TextField(null=True, blank=True)
    twitter_creator = models.CharField(max_length=50, help_text='Twitter handle. E.g. @cotidia', null=True, blank=True)
    twitter_image_src = PublicFileField(upload_to='metadata', null=True, blank=True, help_text='Recommended size: 600 x 335 px')
    twitter_image_alt = models.CharField(max_length=255, null=True, blank=True)

    # Google search data
    google_type = models.CharField(max_length=50, choices=GOOGLE_TYPES, null=True, blank=True)
    google_name = models.CharField(max_length=50, null=True, blank=True)
    google_logo = PublicFileField(upload_to='metadata', null=True, blank=True, help_text='Recommended size: 112 x 112 px (min)')

    class Meta:
        verbose_name = 'MetaData'
        verbose_name_plural = 'MetaDatas'
        ordering = ('order_id',)

    def __str__(self):
        return 'Meta data for {}'.format(self.content_object.__str__())

    def social_networks(self):
        return self.metadatasocial_set.all()


class MetaDataSocial(AbstractOrderable, BaseModel):
    SOCIAL_NETWORKS = (
        ('LINKEDIN', 'LinkedIn'),
        ('TWITTER', 'Twitter'),
        ('FACEBOOK', 'Facebook'),
        ('INSTAGRAM', 'Instagram'),
        ('BEHANCE', 'Behance'),
    )
    member = models.ForeignKey("metadata.MetaData", on_delete=models.CASCADE)
    network = models.CharField(max_length=50, choices=SOCIAL_NETWORKS)
    url = models.URLField(max_length=250)

    class Meta:
        verbose_name = 'MetaData social network'
        verbose_name_plural = 'MetaData social networks'
        ordering = ('order_id',)

    def __str__(self):
        return "{} ({})".format(self.network, self.url)

    def network_label(self):
        return dict(self.SOCIAL_NETWORKS).get(self.network)
