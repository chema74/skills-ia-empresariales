"""Demo local para Skill 03 Forjador de Informes."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import SolicitudForjadorInformes, evaluar_forjador_informes


def main() -> None:
    hallazgos = [
        l.strip()
        for l in (ROOT / "ejemplos" / "hallazgos_demo_forjador.txt").read_text(encoding="utf-8").splitlines()
        if l.strip()
    ]

    entrada = SolicitudForjadorInformes(
        accion="forjar_informe",
        descripcion="Consolidacion semanal de resultados",
        solicitante="direccion_operaciones",
        contexto={"periodo": "semanal"},
        titulo="Informe Ejecutivo Semanal",
        hallazgos=hallazgos,
        metricas={"incidencias": 14, "anomalias_coste": 1, "tickets_cerrados": 27},
        recomendaciones=[
            "Activar mesa de seguimiento con proveedor logistico",
            "Revisar umbrales de alerta para costes",
        ],
    )

    resultado = evaluar_forjador_informes(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_forjador_informes_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()