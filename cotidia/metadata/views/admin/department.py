from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib import messages
from cotidia.admin.views import AdminListView
from django.conf import settings

from cotidia.account.utils import StaffPermissionRequiredMixin

from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminDeleteView,
    AdminCreateView,
    AdminUpdateView
)

from cotidia.metadata.models import Department
from cotidia.metadata.forms.admin.department import (
    DepartmentAddForm,
    DepartmentUpdateForm)


class DepartmentList(AdminListView):
    columns = (
         ("ID", "id"),
         ("Order", "order"),
         ("name", "name"),
    )
    model = Department
    template_type = "centered"


class DepartmentDetail(StaffPermissionRequiredMixin, AdminDetailView):
    model = Department
    permission_required = 'team.change_model'
    fieldsets = [
        {
            "legend": 'Department Details',
            "fields": [
                [
                    {
                        "label": "ID",
                        "field": "id"
                    },
                    {
                        "label": "order id",
                        "field": "order_id"
                    },
                    {
                        "label": "name",
                        "field": "name"
                    },
                ]
            ]
        }
    ]


class DepartmentCreate(StaffPermissionRequiredMixin, AdminCreateView):
    model = Department
    form_class = DepartmentAddForm
    permission_required = 'team.add_model'

    def get_success_url(self):
        messages.success(self.request, 'Department has been created.')
        return reverse('team-admin:department-detail', kwargs={'pk': self.object.id})


class DepartmentUpdate(StaffPermissionRequiredMixin, AdminUpdateView):
    model = Department
    form_class = DepartmentUpdateForm
    permission_required = 'team.change_model'
    fieldsets = [
        {
            "legend": 'Department Details',
            "fields": [
                [
                    {
                        "label": "ID",
                        "field": "id"
                    },
                    {
                        "label": "order id",
                        "field": "order_id"
                    },
                    {
                        "label": "name",
                        "field": "name"
                    },
                ]
            ]
        }
    ]

    def get_success_url(self):
        messages.success(self.request, 'Department details have been updated.')
        return reverse('team-admin:department-detail', kwargs={'pk': self.object.id})


class DepartmentDelete(StaffPermissionRequiredMixin, AdminDeleteView):
    model = Department
    permission_required = 'app.delete_model'

    def get_success_url(self):
        messages.success(self.request, 'Department has been deleted.')
        return reverse('team-admin:department-list')
