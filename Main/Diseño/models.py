from django.db import models

class Diseño(models.Model):
    diseñador = models.CharField(max_length=100)
    diseño = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='diseños/')

    def __str__(self):
        return self.diseño

