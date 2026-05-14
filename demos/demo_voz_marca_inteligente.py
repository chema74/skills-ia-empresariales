"""Demo local para Skill 08 Voz de Marca Inteligente."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import SolicitudVozMarca, evaluar_voz_marca_inteligente


def main() -> None:
    texto = (ROOT / "ejemplos" / "texto_demo_voz_marca.txt").read_text(encoding="utf-8").strip()
    entrada = SolicitudVozMarca(
        accion="adaptar_voz_marca",
        descripcion="Demo local skill 08",
        solicitante="equipo_marketing",
        contexto={"campania": "Q2"},
        texto=texto,
        tono_objetivo="profesional",
        palabras_clave_marca=["clientes", "soluciones"],
    )

    resultado = evaluar_voz_marca_inteligente(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_voz_marca_inteligente_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()