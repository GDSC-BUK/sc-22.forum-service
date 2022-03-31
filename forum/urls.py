"""forum URL Configuration
"""

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

openapi_info = openapi.Info(
    title="SC'22 Forum Service API",
    default_version="v1",
    description="SC'22 Forum Service API Documentation",
    terms_of_service="https://sc22.dev/forum/policies",
    contact=openapi.Contact(email="sc22-forum@sc22.dev"),
)

schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("api/v1/", include("core.urls")),
    path(
        "api/v1/docs/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(
        "api/v1/docs/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
