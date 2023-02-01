from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from flatpages.views import pages_view

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('', pages_view, name='home'),
                  path('pages/', include('flatpages.urls')),

                  path('products/', include('simpleapp.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)