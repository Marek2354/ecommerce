# 🛒 Proyecto E‑commerce (Demo)

Este proyecto es una tienda en línea básica desarrollada con **Django** y **Bootstrap**, que implementa un flujo sencillo de catálogo y carrito de compras.

## 🚀 Funcionalidades implementadas
- **Catálogo de productos**:
  - Visualización en tarjetas con nombre, descripción, precio, stock e imagen.
  - Botón **“Agregar al carrito”** en cada producto.
- **Carrito de compras**:
  - Vista dedicada para mostrar los productos agregados.
  - Botón **“Eliminar”** para quitar productos del carrito.
  - Mensaje claro cuando el carrito está vacío.
- **Navegación**:
  - **Navbar sencillo** con enlace al catálogo y al carrito.
  - **Footer básico** con información de la tienda.
- **Sesiones en Django**:
  - Los productos se guardan en la sesión del usuario, manteniendo el carrito activo mientras navega.

## 📂 Estructura principal
- `views.py`: contiene las funciones `inicio`, `lista_productos`, `agregar_al_carrito`, `ver_carrito`, `eliminar_del_carrito`.
- `urls.py`: define las rutas para catálogo y carrito.
- `templates/tienda/`:
  - `lista_productos.html`: catálogo con tarjetas de productos.
  - `carrito.html`: vista del carrito con opción de eliminar productos.

## 🎨 Mejoras visuales
- Uso de **Bootstrap 5** para un diseño limpio y responsivo.
- Navbar y footer para darle identidad y estructura a la página.
- Tarjetas con sombras y estilo uniforme para los productos.

## 📌 Próximos pasos (opcional)
- Mostrar el **total del carrito**.
- Manejar **cantidades** de productos.
- Autenticación de usuarios y persistencia del carrito en base de datos.
- Flujo de **checkout/pago** y historial de pedidos.

---

✅ Este proyecto demuestra el flujo básico de un e‑commerce: **catálogo → agregar productos → ver carrito → eliminar productos**.  
Es una base sólida para seguir aprendiendo y expandiendo funcionalidades.


## ⚙️ Instalación rápida

1. Clona este repositorio:
   
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo

2. Crea y activa un entorno virtual:
    python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

3. Instala las dependencias:
    pip install -r requirements.txt

4. Aplica las migraciones de Django:
   python manage.py migrate

5. Crea un superusuario (opcional, para acceder al admin):
    python manage.py createsuperuser

6. Inicia el servidor de desarrollo:
    python manage.py runserver

7. Abre en tu navegador:
    http://127.0.0.1:8000/
    




