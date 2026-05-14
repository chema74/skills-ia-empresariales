"""CLI local para ejecutar la skill Puerta de Aprobacion Humana."""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import SolicitudAprobacion, evaluar_puerta_aprobacion_humana


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CLI local de Puerta de Aprobacion Humana")
    parser.add_argument("--accion", required=True, help="Accion a evaluar")
    parser.add_argument("--descripcion", required=True, help="Descripcion de la accion")
    parser.add_argument("--solicitante", required=True, help="Responsable que solicita la accion")
    parser.add_argument("--aprobador", default=None, help="Persona que aprueba la accion")
    parser.add_argument("--aprobada", action="store_true", help="Marca la accion como aprobada")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    solicitud = SolicitudAprobacion(
        accion=args.accion,
        descripcion=args.descripcion,
        solicitante=args.solicitante,
        aprobador=args.aprobador,
        aprobada=args.aprobada,
    )

    resultado = evaluar_puerta_aprobacion_humana(solicitud)
    print(
        json.dumps(
            {
                "nombre_skill": resultado.nombre_skill,
                "estado": resultado.estado,
                "salida": resultado.salida,
                "trazas": resultado.trazas,
                "advertencias": resultado.advertencias,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()