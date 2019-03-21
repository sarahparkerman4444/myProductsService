from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import permissions

# openapi implementation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_info = openapi.Info(
        title="Products Service API",
        default_version='latest',
        description="Test description",
)

schema_view = get_schema_view(
    swagger_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path(r'', include('products.urls')),
    path('health_check/', include('health_check.urls')),
]

urlpatterns += staticfiles_urlpatterns()
