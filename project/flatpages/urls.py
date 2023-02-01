from django.urls import path
from flatpages.views import pages_view, static_pages_id, static_pages

urlpatterns = [
    path('', pages_view),
    path('<int:partner_pages>/', static_pages_id),
    path('<str:partner_pages>/', static_pages),
]