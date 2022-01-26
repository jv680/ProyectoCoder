from django.urls import path
from Restaurante import views

"{% static '/Restaurante/special-dishes.html/' %}"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('menu', views.menu, name='menu'),
    path('bebidas', views.bebidas, name='bebidas'),
    path('reservaciones', views.reservaciones, name='reservaciones'),
]