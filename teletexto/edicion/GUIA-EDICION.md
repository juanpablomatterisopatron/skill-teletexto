# Guía de edición (opcional)

El teletexto graba material limpio. Estos pasos lo convierten en el video final. Son una guía del método; no es un programa
listo para correr, y cada paso se puede hacer con tu editor favorito o pidiéndole a Claude que arme el script.

**Estado de verificación:** el método completo se usó en Mac. Las herramientas que se nombran como alternativas para
Windows y Linux no se probaron aquí; revísalas antes de depender de ellas.

## 0. Qué tienes de la grabación

`camara.mp4` (tu cara, sin fondo cambiado), `pantalla-1.mp4`, `pantalla-2.mp4`… (lo que compartiste) y `marcas.json` (en qué
segundo de la cámara empieza y termina cada pantalla, y las pausas).

## 1. Cortes: «error», «repito», «esto no va»

1. Transcribe la cámara con una herramienta que dé tiempo por palabra (Whisper, Deepgram u otra).
2. Busca las marcas habladas. «Error» o «repito»: corta desde el inicio de esa frase hasta que empieza la repetición buena.
   «Esto no va»: corta ese intento hasta que retomas.
3. Une los trozos buenos con ffmpeg (`concat`) o en tu editor.

## 2. Recortar a la persona (quitar el fondo)

El fondo en vivo del navegador es rápido pero de menor calidad. Para el video final, recorta con un segmentador de personas
sobre `camara.mp4`:

- **Mac:** la API Vision de macOS (`VNGeneratePersonSegmentationRequest`, calidad «accurate»), con un suavizado de la máscara. Es lo que dio mejor resultado.
- **Otros sistemas (sin verificar aquí):** MediaPipe Selfie Segmentation o `rembg` en Python.

Genera una máscara por cuadro y compón a la persona sobre el fondo que elijas.

## 3. Fondo

Un fondo animado (hecho con código, un video en bucle o una imagen) detrás de la persona. Pon la persona a un lado y las
animaciones o los títulos al otro, así el texto no tapa tu cara.

## 4. Pantalla con tu cara en un círculo

Cuando compartiste pantalla, la cámara siguió grabando. Con `marcas.json` sabes en qué segundos hubo pantalla: pon
`pantalla-N.mp4` a pantalla completa y tu cámara recortada en un círculo en una esquina (máscara circular en ffmpeg o en tu editor). Recorta las barras del navegador de la pantalla si salieron.

## 5. Igualar la voz

Si grabaste en dos días o con distinto micrófono, iguala el volumen y el timbre contra la toma que sonó mejor: normaliza a
unos -16 LUFS (`loudnorm` de ffmpeg) y, si hace falta, un ecualizador por bandas para acercar el timbre.

## 6. Revisar antes de exportar (privacidad)

Saca una hoja de cuadros (uno cada 2 a 4 segundos) de todo lo que salió la pantalla compartida. Busca claves, correos,
chats de otras personas y notificaciones. Tapa o congela esos cuadros antes de unir.

## 7. Exportar

MP4 H.264 con audio AAC. Para subir a una comunidad con límite de tamaño, baja a 1280x720 y ~1,8 Mbps con audio de 96 kbps.
