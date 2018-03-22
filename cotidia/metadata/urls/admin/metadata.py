from django.urls import path

from cotidia.metadata.views.admin.metadata import (
    MetaDataCreate,
    MetaDataUpdate,
    MetaDataDelete,
)
from cotidia.metadata.views.admin.metadatasocial import (
    MetaDataSocialCreate,
    MetaDataSocialUpdate,
    MetaDataSocialDelete
)

urlpatterns = [
    path(
        'add/<int:content_type_id>/<int:object_id>/',
        MetaDataCreate.as_view(),
        name='metadata-add'
    ),
    path(
        '<int:pk>/update',
        MetaDataUpdate.as_view(),
        name='metadata-update'
    ),
    path(
        '<int:pk>/delete',
        MetaDataDelete.as_view(),
        name='metadata-delete'
    ),
    path(
        '<int:parent_id>/social/add',
        MetaDataSocialCreate.as_view(),
        name='metadatasocial-add'
    ),
    path(
        '<int:parent_id>/social/<int:pk>/update',
        MetaDataSocialUpdate.as_view(),
        name='metadatasocial-update'
    ),
    path(
        '<int:parent_id>/social/<int:pk>/delete',
        MetaDataSocialDelete.as_view(),
        name='metadatasocial-delete'
    ),
]
