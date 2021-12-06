from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class entradaDiario(models.Model):
	emocion = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=220, blank=True, default='')
	#fecha = datetime.now().strftime("%b-%d-%Y %H-%M")
	fecha = models.DateTimeField(default = timezone.now)

	def __str__(self):
		if self.descripcion == "":
			return self.emocion
		return self.emocion +' - '+ self.descripcion