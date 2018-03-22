from django import forms

from betterforms.forms import BetterModelForm

from cotidia.metadata.models import MetaData


class MetaDataAddForm(BetterModelForm):

    meta_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '3'}),
        required=False
    )

    og_type = forms.ChoiceField(
        choices=(('', ''),) + MetaData.OG_TYPES,
        required=False
    )

    og_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '3'}),
        required=False
    )

    twitter_card = forms.ChoiceField(
        choices=(('', ''),) + MetaData.TWITTER_CARD_TYPES,
        required=False
    )

    twitter_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '3'}),
        required=False
    )

    google_type = forms.ChoiceField(
        choices=(('', ''),) + MetaData.GOOGLE_TYPES,
        required=False
    )

    class Meta:
        model = MetaData
        exclude = ['order_id', 'content_type', 'object_id']
        fieldsets = (
            ('SEO', {
                'fields': (
                    'meta_title',
                    'meta_description',
                    'meta_keywords',
                ),
                'legend': 'SEO'
            }),
            ('Open Graph', {
                'fields': (
                    'og_type',
                    'og_title',
                    'og_description',
                    'og_image'
                ),
                'legend': 'Open Graph'
            }),
            ('Twitter card', {
                'fields': (
                    'twitter_card',
                    'twitter_site',
                    'twitter_title',
                    'twitter_description',
                    'twitter_creator',
                    ('twitter_image_src', 'twitter_image_alt'),
                ),
                'legend': 'Twitter card'
            }),
            ('Google search features', {
                'fields': (
                    'google_type',
                    'google_name',
                    'google_logo'
                ),
                'legend': 'Google search features'
            }),
        )


class MetaDataUpdateForm(MetaDataAddForm):
    class Meta:
        model = MetaData
