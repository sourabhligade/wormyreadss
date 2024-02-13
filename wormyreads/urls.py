from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from books.views import home  # Make sure to import the view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),  # Include the 'books' app URLs
    path('', home, name='home'),  # Serve the home view from the root URL


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


