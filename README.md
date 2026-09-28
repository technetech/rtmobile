# RT Mobile

Landing page en español para rastreo GPS, telemetría y cámaras con streaming.

## Ejecutar localmente

La página es estática y no requiere instalar dependencias ni compilar.

```sh
python -m http.server 4173 --directory dist
```

Abre http://localhost:4173. También puedes abrir `dist/index.html` directamente en el navegador.

## Incluye

- Diseño adaptable a móvil y escritorio.
- Red animada con Canvas y cámara flotante con CSS.
- Catálogo filtrable con fotografías de los productos.
- Demo ilustrativa de cámaras y recorrido GPS interactivo.
- Contacto por WhatsApp, teléfono y correo.
- Controles de animación y soporte para movimiento reducido.

Las demos son ilustrativas y no están conectadas a vehículos reales. Para conectar demostraciones reales, actualiza `openDemo` en `dist/app.js` con los enlaces o reproductores autorizados. No incluyas credenciales privadas en el código del navegador.

## Estructura

```text
dist/
  index.html       Estructura, textos y contactos
  style.css        Estilos y animaciones
  app.js           Catálogo, filtros y demos
  favicon.svg      Icono
  assets/          Imágenes del catálogo
verify.py          Verificación de archivos referenciados
```

Las fuentes de Google requieren conexión a internet y cuentan con fuentes de respaldo.

## Verificar

```sh
node --check dist/app.js
python verify.py
```

## Publicar

Sube el contenido de `dist` a un alojamiento estático, o configura `dist` como directorio de publicación. No se requiere comando de compilación.

Los productos y fotografías provienen de los catálogos proporcionados por RT Mobile. Los precios se omitieron porque los materiales de referencia muestran planes diferentes; confirma tarifas vigentes antes de agregarlas.
