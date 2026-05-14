"""Demo local para Skill 01 Lector Inteligente Documental."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import SolicitudLecturaDocumental, evaluar_lector_inteligente_documental


def main() -> None:
    texto = (ROOT / "ejemplos" / "documento_demo_lector.txt").read_text(encoding="utf-8")
    entrada = SolicitudLecturaDocumental(
        accion="leer_documento",
        descripcion="Demo local skill 01",
        solicitante="equipo_operaciones",
        contexto={"fuente": "ejemplo_local"},
        texto_documento=texto,
        max_secciones=5,
        palabras_clave=["riesgo", "presupuesto", "contingencia"],
    )

    resultado = evaluar_lector_inteligente_documental(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_lector_inteligente_documental_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()