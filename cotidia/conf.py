from django.conf import settings

from appconf import AppConf


class MetaDataConf(AppConf):

    FACEBOOK_APP_ID = "[Not implemented]"

    class Meta:
        prefix = 'metadata'
