from django.urls import path, include

app_name = "metadata"

urlpatterns = [
    path('', include("cotidia.metadata.urls.admin.metadata")),
]
