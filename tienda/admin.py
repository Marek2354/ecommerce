from django.contrib import admin
from .models import Usuario, Producto, Pedido, Carrito

# Personalización de Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')

# Personalización de Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_pedido', 'estado', 'precio_total')
    list_filter = ('estado', 'fecha_pedido')
    search_fields = ('usuario__username', 'direccion')

# Personalización de Carrito
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'subtotal')
    list_filter = ('pedido',)
    search_fields = ('producto__nombre',)

# Personalización de Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo_usuario', 'is_staff', 'is_active')
    list_filter = ('tipo_usuario', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# Personalizar encabezados del admin
admin.site.site_header = "Administración E-commerce"
admin.site.site_title = "Panel de Control E-commerce"
admin.site.index_title = "Bienvenido al Panel de Administración"
