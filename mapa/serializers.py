from rest_framework import serializers
from django.conf import settings
import json
import os
print(settings.GEOJSON_PATH)


class GeoJSONSerializer(serializers.Serializer):
    def to_representation(self, instance):
        # with open(os.path.join(settings.BASE_DIR, 'amva.geojson'), 'r') as f:
        #     

        with open(settings.GEOJSON_PATH, 'r') as f:
            geojson_data = json.load(f)

            print(geojson_data)

            return json.load(f)
        






# from rest_framework import serializers
# from .models import GeoJSON

# class GeoJSONSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GeoJSON
#         fields = ['archivo']
