from cotidia.admin.views import (
    AdminChildCreateView,
    AdminChildUpdateView,
    AdminChildDeleteView,
)

from cotidia.metadata.models import MetaData, MetaDataSocial
from cotidia.metadata.forms.admin.membersocial import (
    MetaDataSocialAddForm,
    MetaDataSocialUpdateForm,
)


class MetaDataSocialCreate(AdminChildCreateView):
    model = MetaDataSocial
    form_class = MetaDataSocialAddForm
    parent_model = MetaData
    parent_model_foreign_key = "member"


class MetaDataSocialUpdate(AdminChildUpdateView):
    model = MetaDataSocial
    form_class = MetaDataSocialUpdateForm
    parent_model = MetaData
    parent_model_foreign_key = "member"


class MetaDataSocialDelete(AdminChildDeleteView):
    model = MetaDataSocial
    parent_model = MetaData
    parent_model_foreign_key = "member"
