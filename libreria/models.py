from django.db import models

# Create your models here.
# Django admin -> User: juanjo -> Password: 123
# Django user -> User: user1 -> Password: useraccount2023+

class libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila
    """
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        
        return super().delete
    """