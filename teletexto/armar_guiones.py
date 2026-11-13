#!/usr/bin/env python3
"""Arma guiones.js para el teletexto con los archivos .txt de la carpeta guiones/.

Cada archivo guiones/<nombre>.txt es un guion: párrafos separados por una línea en blanco. Una línea que empieza con
«§» es una señal (sale chica y en morado, no se lee en voz alta): úsala para títulos, animaciones o lo que hay que
mostrar en pantalla. El título que se ve en la lista es el nombre del archivo, o la primera línea si empieza con «# ».

Se corre cada vez que cambias o agregas un guion:   python3 armar_guiones.py
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CARPETA = AQUI / "guiones"


def main():
    items = []
    for f in sorted(CARPETA.glob("*.txt")):
        texto = f.read_text(encoding="utf-8").strip()
        titulo = f.stem.replace("-", " ").replace("_", " ").capitalize()
        if texto.startswith("# "):
            primera, _, resto = texto.partition("\n")
            titulo, texto = primera[2:].strip(), resto.strip()
        items.append({"id": f.stem, "titulo": titulo, "texto": texto})
    js = "// Lo arma armar_guiones.py desde guiones/. No lo edites a mano.\nwindow.GUIONES = " + \
         json.dumps(items, ensure_ascii=False, indent=1) + ";\n"
    (AQUI / "guiones.js").write_text(js, encoding="utf-8")
    for it in items:
        n = len([p for p in it["texto"].split("\n\n") if p.strip() and not p.startswith("§")])
        print(f'{it["id"]:20} {n:3} párrafos  {it["titulo"]}')


if __name__ == "__main__":
    main()
