from django.db import models

class Menu_Diurno(models.Model):
    plato = (models.CharField(max_length=40))
    precio = (models.IntegerField())

class Menu_Nocturno(models.Model):
    plato = (models.CharField(max_length=40))
    precio = (models.IntegerField())
    
class Bebidas(models.Model):
    bebida = (models.CharField(max_length=40))
    precio = (models.IntegerField())
    