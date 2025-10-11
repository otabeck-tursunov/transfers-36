from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import *
from transfers.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('clubs/', clubs_view, name='clubs'),
    path('clubs/<int:pk>/', club_retrieve_view, name='club-info'),
    path('latest-transfers/', latest_transfers_view, name='latest-transfers'),
    path('players/', players_view, name='players'),
    path('tryouts/', tryouts_view, name='tryouts'),
    path('statistics/', stats_view, name='statistics'),
    path('statistics/top-150-accurate-predictions/', stats_top_150_accurate_predictions, name='top-150'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
