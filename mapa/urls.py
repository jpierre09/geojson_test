from django.http import FileResponse
from django.urls import path
from django.conf import settings
from .views import geojson

# urlpatterns = [
#     path('amva.geojson', lambda request: FileResponse(open(os.path.join(settings.GEOJSON_PATH, 'amva.geojson'), 'rb')))
# ]

urlpatterns = [
    # path('amva.geojson', lambda request: FileResponse(open(settings.GEOJSON_PATH, 'rb'))),
    path('amva.geojson', geojson),
    
]

