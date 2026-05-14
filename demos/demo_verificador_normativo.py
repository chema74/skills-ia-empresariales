"""Demo local para Skill 09 Verificador Normativo."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import ReglaNormativa, SolicitudVerificacionNormativa, evaluar_verificador_normativo


def main() -> None:
    texto = (ROOT / "ejemplos" / "texto_demo_verificador_normativo.txt").read_text(encoding="utf-8")

    reglas = [
        ReglaNormativa(codigo="RN-001", descripcion="Debe mencionar trazabilidad", requerido="trazabilidad", severidad="media"),
        ReglaNormativa(codigo="RN-002", descripcion="Debe incluir revisión humana", requerido="revisión humana", severidad="alta"),
        ReglaNormativa(codigo="RN-003", descripcion="No debe afirmar garantía absoluta", prohibido="garantizado", severidad="alta"),
    ]

    entrada = SolicitudVerificacionNormativa(
        accion="verificar_normativa",
        descripcion="Demo local skill 09",
        solicitante="equipo_compliance",
        contexto={"marco": "interno"},
        texto_objetivo=texto,
        reglas=reglas,
    )

    resultado = evaluar_verificador_normativo(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_verificador_normativo_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()