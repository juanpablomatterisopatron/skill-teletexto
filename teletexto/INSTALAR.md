# Instalar el teletexto

Necesitas: **Python 3** (ya viene en Mac y Linux; en Windows, instálalo desde python.org) y **Google Chrome**. Nada más: no hay que instalar paquetes.

## Con Claude Code (recomendado)

1. Descomprime el zip. Queda una carpeta `teletexto/`.
2. Cópiala a `~/.claude/skills/` (en Windows, `C:\Users\<tu usuario>\.claude\skills\`).
3. En Claude Code pide: «usa el skill teletexto, levanta el servidor y dime la dirección». Claude lo levanta y te da `http://localhost:8765/`.

## Sin Claude Code

1. Descomprime el zip y abre una terminal dentro de la carpeta `teletexto/`.
2. Corre `python3 servidor.py` (en Windows, `python servidor.py`).
3. Abre `http://localhost:8765/` en Chrome.

## Primera vez

- «Encender cámara»: Chrome pide permiso de cámara y micrófono. Acepta y elige tus dispositivos.
- Para «Compartir pantalla» en Mac, el sistema pide el permiso de grabación de pantalla para Chrome (Ajustes del Sistema, Privacidad y seguridad). Reinicia Chrome después de darlo.
- Cambia tu nombre y título del rótulo en los campos «Nombre» y «Título».
- Tus guiones: `.txt` dentro de `guiones/` y corre `python3 armar_guiones.py`. Recarga la página.

## Dónde quedan las tomas

`~/Desktop/teletexto-tomas/<toma>/`. Para cambiar la carpeta: `TELETEXTO_GRABACIONES=/otra/carpeta python3 servidor.py`.

## Si algo falla

- «Este navegador no deja usar la cámara»: abre la página desde `http://localhost:8765/` en Chrome, no con otro navegador.
- Otra app usa la cámara (Zoom, Meet): ciérrala.
- El puerto está ocupado: `python3 servidor.py 8770` y abre `http://localhost:8770/`.
