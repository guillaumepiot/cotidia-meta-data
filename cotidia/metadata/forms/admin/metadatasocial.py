from betterforms.forms import BetterModelForm

from cotidia.metadata.models import MetaDataSocial


class MetaDataSocialAddForm(BetterModelForm):
    class Meta:
        model = MetaDataSocial
        exclude = ['created_at', 'updated_at', 'member']
        fieldsets = (
            ('info', {
                'fields': (
                    ('network', 'url',),
                ),
                'legend': 'MetaData social network'
            }),
        )


class MetaDataSocialUpdateForm(BetterModelForm):
    class Meta:
        model = MetaDataSocial
        exclude = ['created_at', 'updated_at', 'member']
        fieldsets = (
            ('info', {
                'fields': (
                    ('network', 'url',),
                ),
                'legend': 'MetaData social network'
            }),
        )
