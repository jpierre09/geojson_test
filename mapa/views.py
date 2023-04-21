from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GeoJSONSerializer
import json
from django.conf import settings
from django.http import FileResponse
import os


# # Variable global que almacenará el contenido del archivo geojson
# geojson_data = None

# def geojson(request):
#     global geojson_data

#     if geojson_data is None:
#         # Si la variable global está vacía, lee el archivo geojson y almacena su contenido en la variable global
#         with open(settings.GEOJSON_PATH, 'rb') as f:
#             geojson_data = f.read()

#     # Devuelve el contenido almacenado en la variable global como respuesta de archivo
#     return FileResponse(geojson_data, as_attachment=True, filename='amva.geojson')





def geojson(request):
    print(settings.GEOJSON_PATH)
    return FileResponse(open(settings.GEOJSON_PATH, 'rb'))



# class GeoJSONView(APIView):
    
#     def get(self, request, format=None):
#         serializer = GeoJSONSerializer()
#         return Response(serializer.data)
    
    
# with open(settings.GEOJSON_PATH, 'r') as f:
#     geojson_data = json.load(f)

# print(geojson_data)



# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import GeoJSONSerializer
# import json
# import geojson

# # Create your views here.

# class GeoJSONUploadView(APIView):
#     serializer_class = GeoJSONSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             serializer.save()


#             # Leer el archivo GeoJSON y procesar los datos
#             geojson_file = serializer.validated_data['archivo']
#             geojson_data = geojson.load(geojson_file)

#             # Convertir los datos a formato JSON
#             json_data = json.dumps(geojson_data)


#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
