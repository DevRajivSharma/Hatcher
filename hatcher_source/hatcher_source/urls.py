from django.contrib import admin
from django.urls import path,include
import credentials.urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',include('credentials.urls')),
    path('community_post/', include('community_post.urls', namespace='community_post')),
    path('hatcher-admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
