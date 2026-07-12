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
from django.urls import path, include, re_path
from django.conf import settings

# For the admin site branding, we need to import the admin module from config/admin.py
import config.admin  # noqa: F401

#==Api documentation imports==
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from core_apps.users.views import CustomUserDetailView


#===Api authentication imports===
from dj_rest_auth.views import PasswordResetConfirmView
from allauth.account.views import ConfirmEmailView


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
    # Auth dj_rest_auth urls for login, logout, password reset, etc.
    path("api/v1/auth/user/", CustomUserDetailView.as_view(), name="user-detail"),
    re_path(
        r"^api/v1/auth/registration/verify-email/(?P<key>[-:\w]+)/$",
        ConfirmEmailView.as_view(),
        name="verify_email_confirm",
    ),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/auth/password/reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]

# admin.site.site_header = "MEDIUM API Admin"

# admin.site.site_title = "MEDIUM API Admin Portal"

# admin.site.index_title = "Welcome to MEDIUM API Portal"


"""
Available endpoints:

Swagger Docs: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/
Admin Panel: http://localhost:8000/supersecret/

With nginx:
- Swagger: http://localhost:8080/swagger/
- ReDoc: http://localhost:8080/redoc/
- Admin Panel: http://localhost:8080/supersecret/

"""

"""
Auth available endpoints:
- Registration: http://localhost:8000/api/v1/auth/registration/
- Verify Email API: http://localhost:8000/api/v1/auth/registration/verify-email/
- Verify Email Link: http://localhost:8000/api/v1/auth/registration/verify-email/<key>/
- Login: http://localhost:8000/api/v1/auth/login/
- Logout: http://localhost:8000/api/v1/auth/logout/
- Password Reset: http://localhost:8000/api/v1/auth/password/reset/
- Password Reset Confirm: http://localhost:8000/api/v1/auth/password/reset/confirm/<uidb64>/<token>/
- Password Change: http://localhost:8000/api/v1/auth/password/change/
- Logged  in User Details: http://localhost:8000/api/v1/auth/user/
- Refresh Token: http://localhost:8000/api/v1/auth/token/refresh/
- Logout: http://localhost:8000/api/v1/auth/logout/
With nginx:
- Registration: http://localhost:8080/api/v1/auth/registration/
- Verify Email API: http://localhost:8080/api/v1/auth/registration/verify-email/
- Verify Email Link: http://localhost:8080/api/v1/auth/registration/verify-email/<key>/
- Login: http://localhost:8080/api/v1/auth/login/
- Logout: http://localhost:8080/api/v1/auth/logout/
- Password Reset: http://localhost:8080/api/v1/auth/password/reset/
- Password Reset Confirm: http://localhost:8080/api/v1/auth/password/reset/confirm/<uidb64>/<token>/
- Password Change: http://localhost:8080/api/v1/auth/password/change/
- Logged  in User Details: http://localhost:8080/api/v1/auth/user/
- Refresh Token: http://localhost:8080/api/v1/auth/token/refresh/
- Logout: http://localhost:8080/api/v1/auth/logout/
"""

#Chore: Add JWT authentication and admin site branding ,tested auth endpoints with Postman, and updated README.md with new auth endpoints
