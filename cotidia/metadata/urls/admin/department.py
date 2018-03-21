from django.urls import re_path

from cotidia.metadata.views.admin.department import (
    DepartmentList,
    DepartmentCreate,
    DepartmentDetail,
    DepartmentUpdate,
    DepartmentDelete
)

urlpatterns = [
    re_path(r'^$', DepartmentList.as_view(), name='department-list'),
    re_path(r'^add$', DepartmentCreate.as_view(), name='department-add'),
    re_path(r'^(?P<pk>[\d]+)$', DepartmentDetail.as_view(), name='department-detail'),
    re_path(r'^(?P<pk>[\d]+)/update$', DepartmentUpdate.as_view(),
         name='department-update'),
    re_path(r'^(?P<pk>[\d]+)/delete$', DepartmentDelete.as_view(),
         name='department-delete'),
]
