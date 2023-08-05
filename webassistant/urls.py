from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# a list of all the projects urls
urlpatterns = [
    # the url to the admin site
    path('admin/', admin.site.urls),
    # registering all the assistant application urls
    path('', include('assistant.urls')),
]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
