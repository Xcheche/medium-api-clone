"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings


from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions



schema_view = get_schema_view(
    openapi.Info(
        title="MEDIUM  API",
        default_version="v1",
        description="API endpoints for MEDIUM  API Clone Project",
        contact=openapi.Contact(email="checheomenife@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # this is the admin url, it will be used to access the admin panel
    # it is set to a custom URL to enhance security
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
    # Add any additional URL patterns here
]

admin.site.site_header = "MEDIUM API Admin"

admin.site.site_title = "MEDIUM API Admin Portal"

admin.site.index_title = "Welcome to MEDIUM API Portal"


"""
Available endpoints:

Swagger Docs: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/
Admin Panel: http://localhost:8000/supersecret/

"""