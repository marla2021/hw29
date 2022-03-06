from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads.views.location import LocationViewSet

router = routers.SimpleRouter()
router.register(r'location', LocationViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('cat/',include("ads.urls_category")),
    path('ad/', include("ads.urls_ad")),
    path('user/', include("ads.urls_user")),
    path('selection/', include("ads.urls_selection")),
]

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)