#!/usr/bin/env python3
"""Servidor local del teletexto: sirve la página y guarda las grabaciones MIENTRAS se graban.

Cada segundo la página manda el trozo nuevo de la cámara (y de la pantalla, si se está compartiendo) y aquí se agrega
al archivo. Si el navegador se cae a mitad de una toma, lo grabado hasta ese segundo ya está en disco.

    python3 servidor.py [puerto]        (por defecto 8765; solo escucha en 127.0.0.1)

Las tomas quedan en ~/Desktop/teletexto-tomas/<toma>/ (o en la carpeta de la variable TELETEXTO_GRABACIONES): camara.mp4,
pantalla-1.mp4, pantalla-2.mp4... y marcas.json (en qué segundo de la cámara empieza y termina cada pantalla).
"""
import http.server
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = Path(os.environ.get("TELETEXTO_GRABACIONES", str(Path.home() / "Desktop" / "teletexto-tomas")))
NOMBRE = re.compile(r"^[A-Za-z0-9._-]{1,140}$")
TOPE_TROZO = 300 * 1024 * 1024


class Manejador(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(AQUI), **k)

    def log_message(self, formato, *args):
        if self.command != "POST":
            return
        sys.stderr.write("%s %s\n" % (self.log_date_time_string(), formato % args))

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _json(self, codigo, obj):
        cuerpo = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_GET(self):
        if self.path.startswith("/estado"):
            return self._json(200, {"ok": True, "carpeta": str(BASE)})
        return super().do_GET()

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(u.query)
        if u.path != "/subir":
            return self._json(404, {"ok": False, "error": "no_existe"})
        toma = q.get("toma", [""])[0]
        archivo = q.get("archivo", [""])[0]
        modo = q.get("modo", ["agregar"])[0]
        if not NOMBRE.match(toma) or not NOMBRE.match(archivo) or archivo.startswith("."):
            return self._json(400, {"ok": False, "error": "nombre"})
        largo = int(self.headers.get("Content-Length") or 0)
        if largo > TOPE_TROZO:
            return self._json(413, {"ok": False, "error": "muy_grande"})
        datos = self.rfile.read(largo)
        carpeta = BASE / toma
        carpeta.mkdir(parents=True, exist_ok=True)
        ruta = carpeta / archivo
        with open(ruta, "wb" if modo == "nuevo" else "ab") as f:
            f.write(datos)
        return self._json(200, {"ok": True, "bytes": ruta.stat().st_size})


def main():
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    BASE.mkdir(parents=True, exist_ok=True)
    print("Teletexto en http://localhost:%d/  ·  grabaciones en %s" % (puerto, BASE), flush=True)
    http.server.ThreadingHTTPServer(("127.0.0.1", puerto), Manejador).serve_forever()


if __name__ == "__main__":
    main()
