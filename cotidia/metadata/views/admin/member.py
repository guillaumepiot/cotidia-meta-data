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
from cotidia.metadata.forms.admin.member import (
    MetaDataAddForm,
    MetaDataUpdateForm,
)


class MetaDataFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label="Name",
        method="filter_name"
    )

    class Meta:
        model = MetaData
        fields = ['name', 'active']

    def filter_name(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value)
        )


class MetaDataList(AdminListView):
    columns = (
        ('Name', 'name'),
        ('Role', 'role'),
        ('Slug', 'slug'),
        ('Active', 'active'),
        ('Order', 'order'),
    )
    model = MetaData
    filterset = MetaDataFilter
    template_type = "centered"


class MetaDataDetail(AdminDetailView):
    model = MetaData
    fieldsets = [
        {
            "legend": "MetaData details",
            "fields": [
                [
                    {
                        "label": "Name",
                        "field": "name",
                    }
                ],
                {
                    "label": "Role",
                    "field": "role",
                },
                {
                    "label": "Slug",
                    "field": "slug",
                },
                {
                    "label": "Biography",
                    "field": "bio",
                },
                [
                    {
                        "label": "Email",
                        "field": "email",
                    },
                    {
                        "label": "Phone",
                        "field": "phone",
                    }
                ],
                {
                    "label": "Active",
                    "field": "active",
                },
            ]
        },
        {
            "legend": "Photo",
            "fields": [
                {
                    "label": "Photo",
                    "field": "photo",
                }
            ]
        },
        {
            "legend": "Social networks",
            "template_name": "admin/team/member/social_networks.html"
        }
    ]


class MetaDataCreate(AdminCreateView):
    model = MetaData
    form_class = MetaDataAddForm


class MetaDataUpdate(AdminUpdateView):
    model = MetaData
    form_class = MetaDataUpdateForm


class MetaDataDelete(AdminDeleteView):
    model = MetaData
