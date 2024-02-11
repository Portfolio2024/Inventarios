from django.db import models
from django.contrib.auth.models import User

CATEGORIA = (
    ('Electronicos', 'Electronicos'),
    ('Ropa', 'Ropa'),
    ('Comida', 'Comida')
)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    teléfono = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    categoria = models.CharField(max_length=50, choices = CATEGORIA, null = True)
    cantidad = models.PositiveIntegerField(null=True)
    precio = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.nombre} - {self.cantidad}'
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    
class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    perfil = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cantidadPedida = models.PositiveIntegerField(null=True)
    precioPedido = models.PositiveIntegerField(null=True)
    fechaPedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.producto} ordenado por {self.perfil.username}'
    
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'


    



