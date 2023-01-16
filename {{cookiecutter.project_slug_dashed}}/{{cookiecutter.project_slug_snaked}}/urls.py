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

    path(
        "password/reset/confirm/<uidb64>/<token>/",
        TemplateView.as_view(template_name="accounts/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),

    # v1 APIs
    path(
        "api/v1/",
        include(
            (
                [
                    path("auth/", include("dj_rest_auth.urls")),
                    path("auth/registration/account-confirm-email/<str:key>/", confirm_email),
                    path("auth/registration/", include("dj_rest_auth.registration.urls")),
                ],
                "v1",
            ),
            namespace="v1",
        ),
    ),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Swagger
api_info = openapi.Info(
    title="{{ cookiecutter.project_name }} API",
    default_version="v1",
    description="API documentation for {{ cookiecutter.project_name }}",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),
]


admin.site.site_header = "{{ cookiecutter.project_name }}"
admin.site.site_title = "{{ cookiecutter.project_name }} Admin Portal"
admin.site.index_title = "{{ cookiecutter.project_name }} Admin"
