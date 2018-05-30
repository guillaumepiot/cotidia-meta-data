from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from cotidia.admin.views import (
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        ct = ContentType.objects.get_for_id(self.content_type_id)
        parent = ct.get_object_for_this_type(pk=self.object_id)
        context['parent'] = parent.parent
        context['parent_app_label'] = parent.parent._meta.app_label
        context['parent_model_name'] = parent.parent._meta.model_name
        return context

    def get(self, *args, **kwargs):
        self.content_type_id = kwargs.get('content_type_id')
        self.object_id = kwargs.get('object_id')
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.content_type_id = kwargs.get('content_type_id')
        self.object_id = kwargs.get('object_id')
        return super().post(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.content_type_id = self.content_type_id
        self.object.object_id = self.object_id
        self.object.save()
        return super().form_valid(form)

    def build_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        else:

            url_name = "{}-admin:{}-update".format(
                self.parent_model._meta.app_label,
                self.parent_model._meta.model_name
            )
            return reverse(url_name, args=[self.object.id])


class MetaDataUpdate(AdminUpdateView):
    model = MetaData
    form_class = MetaDataUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        ct = ContentType.objects.get_for_id(self.object.content_type_id)
        parent = ct.get_object_for_this_type(pk=self.object.object_id)
        context['parent'] = parent.parent
        context['parent_app_label'] = parent.parent._meta.app_label
        context['parent_model_name'] = parent.parent._meta.model_name
        return context

    def build_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        else:

            url_name = "{}-admin:{}-update".format(
                self.parent_model._meta.app_label,
                self.parent_model._meta.model_name
            )
            return reverse(url_name, args=[self.object.id])

    def build_detail_url(self):
        return None


class MetaDataDelete(AdminDeleteView):
    model = MetaData
