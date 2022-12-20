from django.urls import path
from .views import SensorView, SensorView_Update, MeasurementView_Create


urlpatterns = [
    path('sensor/', SensorView.as_view(), name='smart_home'),
    path('sensor/<int:pk>/', SensorView_Update.as_view()),
    path('measurement/', MeasurementView_Create.as_view())
]

