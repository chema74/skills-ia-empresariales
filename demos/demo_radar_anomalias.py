"""Demo local para Skill 02 Radar de Anomalias."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import SolicitudRadarAnomalias, evaluar_radar_anomalias


def main() -> None:
    lineas = (ROOT / "ejemplos" / "serie_demo_radar_anomalias.txt").read_text(encoding="utf-8").splitlines()
    serie = [float(x.strip()) for x in lineas if x.strip()]

    entrada = SolicitudRadarAnomalias(
        accion="detectar_anomalias",
        descripcion="Demo local skill 02",
        solicitante="equipo_finanzas",
        contexto={"fuente": "serie_demo"},
        serie=serie,
        umbral_desviaciones=2.0,
    )

    resultado = evaluar_radar_anomalias(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_radar_anomalias_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()