"""Demo local V2 para Puerta de Aprobacion Humana."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import SolicitudAprobacion, evaluar_puerta_aprobacion_humana


def main() -> None:
    solicitud = SolicitudAprobacion(
        accion="aprobar_pago",
        descripcion="Pago de proveedor critico del mes",
        solicitante="equipo_finanzas",
        aprobador="responsable_operaciones",
        aprobada=True,
    )

    resultado = evaluar_puerta_aprobacion_humana(solicitud)

    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))

    ruta = ROOT / "evidencias" / "salidas" / "demo_puerta_aprobacion_humana_v2.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()