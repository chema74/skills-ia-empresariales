"""Demo V7: evidencia de auditoria tecnica y gobernanza."""

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.core.gobernanza import cargar_politicas, cargar_registro_cambios


def main() -> None:
    politicas = cargar_politicas()
    cambios = cargar_registro_cambios()

    evidencia = {
        "release": "v7-governanza",
        "fecha": date.today().isoformat(),
        "estado": "aprobada",
        "resultados": {
            "gobernanza_versionada": len(politicas) > 0,
            "registro_cambios_gobernanza": len(cambios) > 0,
            "politica_aprobar_pago_v1": politicas.get("aprobar_pago").version == "v1.0.0"
            if politicas.get("aprobar_pago")
            else False,
        },
        "resumen": {
            "total_politicas": len(politicas),
            "total_cambios_gobernanza": len(cambios),
        },
    }

    ruta = ROOT / "evidencias" / "salidas" / "demo_v7_auditoria_gobernanza.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(evidencia, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(evidencia, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
