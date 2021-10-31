from rest_framework import viewsets
from .models import BaseMap
from .serializers import BaseMapSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import BaseMap
from .serializers import BaseMapSerializer
from rest_framework.decorators import api_view

class BaseMapViewSet(viewsets.ModelViewSet):
    serializer_class = BaseMapSerializer
    queryset = BaseMap.objects.all()
# class BaseMapViewSet(viewsets.ViewSet):
#     serializer_class = BaseMapSerializer
#
#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             url = serializer.validated_data.get('url')
#             message = f'The information about the basemap is:{name}{url}'
#             serializer.save()
#
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def retrieve(self, reques, pk=None):
#         basemap = BaseMap.objects.get(pk=pk)
#         serializer = BaseMapSerializer(basemap)
#         return Response(serializer.data)
#
#     def list(self, request):
#         basemap = BaseMap.objects.all()
#         serializer = BaseMapSerializer(basemap, many=True)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         basemap = BaseMap.objects.get(pk=pk)
#         serializer = BaseMapSerializer(instance=basemap, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def partial_update(self, request, pk=None):
#         basemap = BaseMap.objects.get(pk=pk)
#         serializer = BaseMapSerializer(instance=basemap, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         basemap = BaseMap.objects.get(pk=pk)
#         basemap.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

