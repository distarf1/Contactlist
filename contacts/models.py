from django.db import models

# Create your models here.
class Contact(models.Model):
    avatar = models.ImageField(upload_to='contact', null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50)
    fechanacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    telefono = models.CharField(max_length=15, null=True, blank=True, verbose_name='Teléfono')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        # Devuelve el nombre y apellidos si ambos existen
        if self.nombre and self.apellidos:
            return f"{self.nombre} {self.apellidos}"
        elif self.nombre:
            return self.nombre
        elif self.apellidos:
            return self.apellidos
        else:
            return self.email 

