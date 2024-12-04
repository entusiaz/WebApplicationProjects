from django.urls import path
from api import views

urlpatterns = [
    path('plot-shape/', views.plotShape, name='plot-shape'),
]