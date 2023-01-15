from django.urls import path
from .views import *
urlpatterns = [
    path('', pages_view),
    path('<int:partner_pages>/', static_pages_id),
    path('<str:partner_pages>/', static_pages),
]