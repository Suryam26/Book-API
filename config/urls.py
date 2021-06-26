from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version="v1",
        description="An API to Retrieve, Upload and Update books.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suryam.jain@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Browsable API Auth
    path('auth/', include('rest_framework.urls')),

    # Authentication End-Points
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # JWT Auth
    path('jwt/login/', TokenObtainPairView.as_view(), name='jwt_login'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API
    path('', include('books.urls')),

    # Schema and Docs
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
