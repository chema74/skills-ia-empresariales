"""Demo V6: orquestador multi-skill con tres pipelines empresariales."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import (
    PIPELINE_CLIENTE_COMUNICACION,
    PIPELINE_CUMPLIMIENTO_PUBLICACION,
    PIPELINE_RIESGO_INFORME,
    SolicitudOrquestacion,
    evaluar_orquestador_multiskill,
)


def _guardar(nombre: str, payload: dict[str, object]) -> None:
    ruta = ROOT / "evidencias" / "salidas" / nombre
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _serializar(resultado: object) -> dict[str, object]:
    return {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }


def main() -> None:
    riesgo = evaluar_orquestador_multiskill(
        SolicitudOrquestacion(
            accion="orquestar",
            descripcion="demo_v6",
            solicitante="orquestador",
            contexto={},
            pipeline_id=PIPELINE_RIESGO_INFORME,
            entrada_pipeline={
                "titulo": "Informe Operativo V6",
                "factores": [
                    {"nombre": "continuidad", "severidad": 8, "peso": 4.0},
                    {"nombre": "cumplimiento", "severidad": 7, "peso": 3.0},
                ],
            },
        )
    )

    cumplimiento = evaluar_orquestador_multiskill(
        SolicitudOrquestacion(
            accion="orquestar",
            descripcion="demo_v6",
            solicitante="cumplimiento",
            contexto={},
            pipeline_id=PIPELINE_CUMPLIMIENTO_PUBLICACION,
            entrada_pipeline={
                "texto_objetivo": "Comunicacion sin consentimiento y con promesa garantizado.",
                "reglas": [
                    {
                        "codigo": "RG-CONSENT",
                        "descripcion": "Debe incluir consentimiento",
                        "requerido": "consentimiento",
                        "severidad": "alta",
                    },
                    {
                        "codigo": "RG-PROMESA",
                        "descripcion": "No promesas absolutas",
                        "prohibido": "garantizado",
                        "severidad": "media",
                    },
                ],
            },
        )
    )

    cliente = evaluar_orquestador_multiskill(
        SolicitudOrquestacion(
            accion="orquestar",
            descripcion="demo_v6",
            solicitante="cx",
            contexto={},
            pipeline_id=PIPELINE_CLIENTE_COMUNICACION,
            entrada_pipeline={
                "cliente_id": "CLI-77",
                "eventos": [
                    {
                        "fecha": "2026-05-10T10:00:00",
                        "tipo": "reunion",
                        "detalle": "revision trimestral",
                        "origen": "crm",
                    }
                ],
                "tono_objetivo": "ejecutivo",
                "texto_base": "Seguimos acompanando la operacion con foco en continuidad del servicio.",
                "palabras_clave_marca": ["servicio", "continuidad"],
            },
        )
    )

    _guardar("demo_v6_pipeline_riesgo_informe.json", _serializar(riesgo))
    _guardar("demo_v6_pipeline_cumplimiento_publicacion.json", _serializar(cumplimiento))
    _guardar("demo_v6_pipeline_cliente_comunicacion.json", _serializar(cliente))

    print(
        json.dumps(
            {
                "evidencias_generadas": [
                    "demo_v6_pipeline_riesgo_informe.json",
                    "demo_v6_pipeline_cumplimiento_publicacion.json",
                    "demo_v6_pipeline_cliente_comunicacion.json",
                ]
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
