"""{{ cookiecutter.project_slug }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from allauth.account.views import confirm_email
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/account-confirm-email/<str:key>/", confirm_email),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        TemplateView.as_view(template_name="accounts/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Swagger
api_info = openapi.Info(
    title="{{ cookiecutter.project_description }} API",
    default_version="v1",
    description="API documentation for {{ cookiecutter.project_description }}",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),
]


admin.site.site_header = "{{ cookiecutter.project_description }}"
admin.site.site_title = "{{ cookiecutter.project_description }} Admin Portal"
admin.site.index_title = "{{ cookiecutter.project_description }} Admin"
