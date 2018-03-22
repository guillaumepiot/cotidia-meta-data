import django_filters

from django.db.models import Q

from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminCreateView,
    AdminUpdateView,
    AdminDeleteView,
)

from cotidia.metadata.models import MetaData
from cotidia.metadata.forms.admin.metadata import (
    MetaDataAddForm,
    MetaDataUpdateForm,
)


class MetaDataCreate(AdminCreateView):
    model = MetaData
    form_class = MetaDataAddForm


class MetaDataUpdate(AdminUpdateView):
    model = MetaData
    form_class = MetaDataUpdateForm


class MetaDataDelete(AdminDeleteView):
    model = MetaData
