from django.conf.urls import url, include

from cotidia.metadata.views.admin.member import (
    MetaDataList,
    MetaDataCreate,
    MetaDataDetail,
    MetaDataUpdate,
    MetaDataDelete,
)
from cotidia.metadata.views.admin.department import (
    DepartmentList,
    DepartmentCreate,
    DepartmentDetail,
    DepartmentUpdate,
    DepartmentDelete,
)
from cotidia.metadata.views.admin.membersocial import (
    MetaDataSocialCreate,
    MetaDataSocialUpdate,
    MetaDataSocialDelete
)

urlpatterns = [
    url(
        r'^$',
        MetaDataList.as_view(),
        name='member-list'
    ),
    url(
        r'^add$',
        MetaDataCreate.as_view(),
        name='member-add'
    ),
    url(
        r'^(?P<pk>[\d]+)$',
        MetaDataDetail.as_view(),
        name='member-detail'
    ),
    url(
        r'^(?P<pk>[\d]+)/update$',
        MetaDataUpdate.as_view(),
        name='member-update'
    ),
    url(
        r'^(?P<pk>[\d]+)/delete$',
        MetaDataDelete.as_view(),
        name='member-delete'
    ),
    url(
        r'^(?P<parent_id>[\d]+)/social/add$',
        MetaDataSocialCreate.as_view(),
        name='membersocial-add'
    ),
    url(
        r'^(?P<parent_id>[\d]+)/social/(?P<pk>[\d]+)/update$',
        MetaDataSocialUpdate.as_view(),
        name='membersocial-update'
    ),
    url(
        r'^(?P<parent_id>[\d]+)/social/(?P<pk>[\d]+)/delete$',
        MetaDataSocialDelete.as_view(),
        name='membersocial-delete'
    ),
]
