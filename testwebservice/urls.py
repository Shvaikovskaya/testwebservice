from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework')),
    path('load/users/<owner>', views.get_user_data, name='get_user_data'),
    path('load/orgs/<owner>', views.get_org_data, name='get_org_data'),
    path('api/', include('api.urls')),
    path('', views.repositories, name='repositories'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
