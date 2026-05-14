"""Demo local para Skill 07 Enrutador Inteligente."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import SolicitudEnrutamiento, evaluar_enrutador_inteligente


def main() -> None:
    intencion = (ROOT / "ejemplos" / "intencion_demo_enrutador.txt").read_text(encoding="utf-8").strip()
    entrada = SolicitudEnrutamiento(
        accion="enrutar_intencion",
        descripcion="Demo local skill 07",
        solicitante="orquestador_local",
        contexto={"canal": "interno"},
        intencion=intencion,
        metadatos={"prioridad": "media"},
    )

    resultado = evaluar_enrutador_inteligente(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_enrutador_inteligente_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()