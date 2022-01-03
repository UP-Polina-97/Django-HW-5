# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer,SensorDetailSerializer

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class MeasurmentsList(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer

    def mesurment_add(self, serializer):
        serializer.save()


class SensorList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def sensor_make(self, serializer):
        serializer.save()


class SensorDetail(RetrieveDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer