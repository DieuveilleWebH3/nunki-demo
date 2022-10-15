

from django.urls import path, include, re_path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


schema_view = get_schema_view(
    openapi.Info(
        title="Nunki Demo API",
        default_version='v1',
        description="Nunki Demo API by Dieuveille BOUSSA ELLENGA",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="dieuveilleellenga@gmail.com"),
        license=openapi.License(name="Dieuveille BOUSSA ELLENGA License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# schema_view = get_swagger_view(title="Swagger Docs")

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
         
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^docs/', schema_view),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
