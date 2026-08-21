from django.db import models
from django.contrib.auth.models import AbstractUser

# Extensión del modelo de usuario de Django
class Usuario(AbstractUser):
    tipo_usuario = models.CharField(
        max_length=20,
        choices=[('cliente', 'Cliente'), ('admin', 'Administrador'), ('operador', 'Operador')],
        default='cliente'
    )

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='pendiente')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    direccion = models.CharField(max_length=200)

class Carrito(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carrito"

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"
