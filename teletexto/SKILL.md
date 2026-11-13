---
name: teletexto
description: Teletexto (teleprompter) para grabar videos mirando a la cámara. Una página local que muestra el guion subiendo solo cerca del lente, graba la cámara limpia y cada pantalla compartida en archivos aparte, los guarda mientras grabas y deja un archivo de marcas con los tiempos. Usar cuando se pida grabar un video leyendo un guion, un teletexto o teleprompter, un curso, un video de ventas o una presentación en cámara, o armar un teletexto a la medida (otro diseño, otro flujo de guiones).
---

# Teletexto: graba videos leyendo un guion que avanza solo

Una página que se abre en Chrome. Arriba, cerca de la cámara, el guion sube a tu ritmo de lectura. Abajo, la vista
previa de lo que se graba. El texto no sale en el video.

## Qué hace

- **Guion que avanza solo** con velocidad ajustable (flechas), letra ajustable, espejo opcional para vidrio de teleprompter y pausa.
- **Cámara limpia por defecto**: el fondo, el rótulo y las animaciones se ponen después, en la edición, con más calidad.
  También hay fondo en vivo (red animada, estudio, desenfoque o una imagen tuya) para un video rápido sin edición.
- **Compartir pantalla** sin dejar de grabar la cámara: la pantalla se guarda en su propio archivo y la cámara sigue,
  para poner después tu cara en un círculo sobre la pantalla.
- **Se guarda mientras grabas**: cada segundo, un servidor local (`servidor.py`) agrega el trozo nuevo al archivo. Si el
  navegador se cae a mitad de una toma, lo grabado hasta ese segundo ya está en disco.
- **Marcas** (`marcas.json` por toma): en qué segundo de la cámara empieza y termina cada pantalla, dónde pausaste y el guion leído.
- **Varios guiones**: pones archivos `.txt` en `guiones/`, corres `python3 armar_guiones.py` y aparecen en la lista.

## Cómo se usa

1. Levanta el servidor: `python3 servidor.py` (puerto 8765 por defecto, solo escucha en tu computador).
2. Abre `http://localhost:8765/` en Chrome. «Encender cámara», elige cámara y micrófono; la barra de colores muestra si te escucha.
3. «Grabar» (o la tecla R): cuenta 3, 2, 1 y el texto parte. «Detener» cierra la toma.
4. La toma queda en `~/Desktop/teletexto-tomas/<toma>/` (o en la carpeta de la variable `TELETEXTO_GRABACIONES`):
   `camara.mp4`, `pantalla-1.mp4`, … y `marcas.json`.

Teclas: Espacio para o sigue el texto, flechas arriba y abajo cambian la velocidad, izquierda y derecha retroceden o
adelantan, + y − cambian la letra, R graba o detiene, Inicio vuelve al principio.

## Marcas habladas al grabar (para la edición)

No hacen falta botones: se dicen en voz alta y se cortan después, con una transcripción con tiempos por palabra.

- **«error»** o **«repito»**: corta desde el inicio de esa frase hasta la repetición buena.
- **«esto no va»**: descarta ese intento hasta que retomas la grabación.

Haz una pausa de un segundo antes de repetir: el corte queda más limpio.

## Guiones y señales

En un guion, los párrafos van separados por una línea en blanco. Una línea que empieza con `§` es una **señal**: sale chica y en
morado y no se lee en voz alta (título del bloque, «muestra la pantalla», «aquí va una animación»). Hay un ejemplo en `guiones/ejemplo.txt`.

## Cuidado al compartir pantalla entera

Al compartir toda la pantalla sale todo lo que haya en ella: archivos con claves, notificaciones, barras laterales de otros
chats. Antes de unir el video, revisa hojas de cuadros (un cuadro cada 2 a 4 segundos) y tapa o congela lo sensible. Mejor
todavía: cierra lo que no vas a mostrar antes de grabar.

## Edición (opcional)

Ver `edicion/GUIA-EDICION.md`: recorte de la persona, fondo, cara en círculo sobre la pantalla e igualar la voz.

## Hacerlo a la medida

Es una sola página (`index.html`) y un servidor chico (`servidor.py`). Se puede pedir a Claude que lo adapte: otro diseño,
tu marca, un formato vertical, guiones que se arman desde tus documentos, subida de las tomas a donde quieras.

## Límites que conviene saber

- Probado con Chrome. Necesita permiso de cámara y micrófono; para compartir pantalla, el permiso de grabación de pantalla del sistema.
- El recorte de fondo en vivo baja un modelo de internet la primera vez; sin internet se graba igual con «Sin cambiar el fondo».
- El MP4 del navegador no pasa de 4 GB: las tomas muy largas se parten solas en `camara-2`, `camara-3` (con su inicio en `marcas.json`).
- Las preferencias y el guion editado quedan solo en ese navegador.
