# Cotidia meta data

A plugin to manage meta data on any content:

- Open Graph
- Twitter cards
- Google search features

```console
$ pip install -e git+git@code.cotidia.com:cotidia/meta-data.git#egg=cotidia-meta-data
```

## Settings

Set Facebook app id:

```python
METADATA_FACEBOOK_APP_ID = "1234"
```

Add `cotidia.metadata` to your INSTALLED_APPS:

```python
INSTALLED_APPS=[
    ...
    "cotidia.metadata",

]
```

Add meta data admin to urls:

```
urlpatterns = [
    path('admin/meta-data/', include('cotidia.metadata.urls.admin', namespace='metadata-admin')),
]

## Template tags

### Get meta data instance

Return the instance meta data for a given object, return None if it doesn't exist.

```html
{% load metadata_tags %}
{% get_meta_data object as metadata %}
```

## Context processor

```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
            ...
                'cotidia.metadata.context_processor.metadata_settings',
            ],
        },
    },
]
```
