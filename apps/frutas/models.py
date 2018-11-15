from django.db import models

# Create your models here.
"""
class Fruta(models.Model):
	id_fruta = models.AutoField(primary_key=True)
	nombre = models.CharField(max_lenght = 20)
	#precio
class Compra(models.Model):
	id_compra = models.AutoField(primary_key=True)
	id_fruta = models.ManyToOne(Fruta)
	id_comprador = models.ForeignKey('auth.User',on_delete = models.CASCADE)
	#OneToOne
	#ManyToMany
	cantidad = models.IntegerField()
	precioTotal = models.FloatField()

"""