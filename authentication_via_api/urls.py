from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),

    path(
      "api/doc/swagger/",
      SpectacularSwaggerView.as_view(url_name="schema"),
      name="swagger-ui",
    ),

]
