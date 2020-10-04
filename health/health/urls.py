from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('accounts.urls')),
    path('api/', include('history.api.urls')),
    path('chat/', include('chat.urls')),
    path('blog/', include('blog.urls')),
    path('', include(('events.urls', 'events'), namespace='calendar')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Social Authentication urls
urlpatterns += path('oauth/', include('social_django.urls'), name='social_auth'),
