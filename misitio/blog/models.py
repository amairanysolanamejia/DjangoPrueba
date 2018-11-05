from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

		def __str__(self):
			return self.title


 # Esto fue un ejemplo ya resuelto, pero debemos hacer otro
class Producto(models.Model):
 	nombre = models.CharField(max_length=200)
 	caracteristicas = models.TextField()
 	fecha_fabricacion = models.DateTimeField(default=timezone.now)
 	fecha_caducidad = models.DateTimeField(blank=True, null=True)
 	precio = models.DecimalField(max_digits=6, decimal_places=2)

 # DecimalField¶

 # class DecimalField(max_digits=None, decimal_places=None, **options)[source]¶

 # A fixed-precision decimal number, represented in Python by a Decimal instance. Has two required arguments:

 # DecimalField.max_digits¶

 #     The maximum number of digits allowed in the number. Note that this number must be greater than or equal to decimal_places.

 # DecimalField.decimal_places¶

 #     The number of decimal places to store with the number.

 # For example, to store numbers up to 999 with a resolution of 2 decimal places, you’d use:

 # models.DecimalField(..., max_digits=5, decimal_places=2)



 #    def costo(self):
 #precio = models.DecimalField(max_digits=6, decimal_places=2)
 #        self.costo_producto = timezone.now()
 #        self.save()

 #    def __str__(self):
 #        return self.nombre