from betterforms.forms import BetterModelForm

from cotidia.metadata.models import MetaData


class MetaDataAddForm(BetterModelForm):
    class Meta:
        model = MetaData
        exclude = ['created_at', 'updated_at', 'order_id']
        fieldsets = (
            ('info', {
                'fields': (
                    ('first_name', 'last_name'),
                    'slug',
                    'role',
                    'department',
                    'bio',
                    ('email', 'phone'),
                    'active',
                ),
                'legend': 'MetaData details'
            }),
            ('photo', {
                'fields': (
                    'photo',
                ),
                'legend': 'Photo'
            }),
        )


class MetaDataUpdateForm(BetterModelForm):
    class Meta:
        model = MetaData
        exclude = ['created_at', 'updated_at', 'order_id']
        fieldsets = (
            ('info', {
                'fields': (
                    ('first_name', 'last_name'),
                    'role',
                    'department',
                    'slug',
                    'bio',
                    ('email', 'phone'),
                    'active',
                ),
                'legend': 'MetaData details'
            }),
            ('photo', {
                'fields': (
                    'photo',
                ),
                'legend': 'Photo'
            }),
        )
