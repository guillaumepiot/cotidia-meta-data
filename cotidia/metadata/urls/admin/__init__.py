from django.urls import path, include

app_name = "team"
urlpatterns = [
    path('member/',
            include("cotidia.metadata.urls.admin.members")),
    path('department/',
            include("cotidia.metadata.urls.admin.department"))
    ]
