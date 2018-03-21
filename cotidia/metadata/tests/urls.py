from django.urls import path, include

urlpatterns = [
    path('team', include("cotidia.metadata.urls.admin", namespace="team-admin")),
    path('account', include("cotidia.account.urls.admin",
                            namespace="account-admin")),
    path('mail', include("cotidia.mail.urls",
                         namespace="mail-admin")),
    path('admin', include("cotidia.admin.urls.admin",
                          namespace="generic-admin")),
    path('admin', include("cotidia.file.urls.admin",
                          namespace="file-admin")),
    path('dashboard', lambda x: None, name="dashboard")
    ]
