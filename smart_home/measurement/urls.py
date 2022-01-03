from django.urls import path

from .views import MeasurmentsList, SensorList, SensorDetail

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('measurements/', MeasurmentsList.as_view()),
    path('sensors/', SensorList.as_view()),
    path('sensordetail/', SensorDetail.as_view()),
]
