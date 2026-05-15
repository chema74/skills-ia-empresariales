"""Demo V5: flujos de integracion y evidencias de calidad."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import (
    FactorRiesgo,
    ReglaNormativa,
    SolicitudAprobacion,
    SolicitudEnrutamiento,
    SolicitudForjadorInformes,
    SolicitudPulsoRiesgo,
    SolicitudVerificacionNormativa,
    evaluar_enrutador_inteligente,
    evaluar_forjador_informes,
    evaluar_puerta_aprobacion_humana,
    evaluar_pulso_riesgo,
    evaluar_verificador_normativo,
)


def _serializar_resultado(resultado: object) -> dict[str, object]:
    return {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }


def _guardar(nombre: str, payload: dict[str, object]) -> None:
    ruta = ROOT / "evidencias" / "salidas" / nombre
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    # Flujo 1: enrutar -> pulso_riesgo -> informe.
    enrutado = evaluar_enrutador_inteligente(
        SolicitudEnrutamiento(
            accion="enrutar",
            descripcion="demo_v5",
            solicitante="orquestador",
            contexto={},
            intencion="Necesito evaluar riesgo operativo y preparar informe ejecutivo",
        )
    )
    riesgo = evaluar_pulso_riesgo(
        SolicitudPulsoRiesgo(
            accion="calcular_riesgo",
            descripcion="demo_v5",
            solicitante="orquestador",
            contexto={},
            factores=[
                FactorRiesgo(nombre="continuidad", severidad=8, peso=4.0),
                FactorRiesgo(nombre="cumplimiento", severidad=7, peso=3.0),
            ],
        )
    )
    informe = evaluar_forjador_informes(
        SolicitudForjadorInformes(
            accion="forjar_informe",
            descripcion="demo_v5",
            solicitante="orquestador",
            contexto={},
            titulo="Informe Integrado V5",
            hallazgos=[f"Nivel detectado: {riesgo.salida['nivel_riesgo']}"],
            metricas={"puntuacion_riesgo": riesgo.salida["puntuacion"]},
            recomendaciones=riesgo.salida["recomendaciones"],
        )
    )
    evidencia_1 = {
        "flujo": "enrutado_riesgo_informe",
        "pasos": [
            _serializar_resultado(enrutado),
            _serializar_resultado(riesgo),
            _serializar_resultado(informe),
        ],
    }

    # Flujo 2: verificacion normativa -> bloqueo por puerta humana.
    verificacion = evaluar_verificador_normativo(
        SolicitudVerificacionNormativa(
            accion="verificar_normativa",
            descripcion="demo_v5",
            solicitante="cumplimiento",
            contexto={},
            texto_objetivo="Comunicacion sin consentimiento y con promesa garantizado.",
            reglas=[
                ReglaNormativa(
                    codigo="RG-CONSENT-01",
                    descripcion="Debe incluir consentimiento",
                    requerido="consentimiento",
                    severidad="alta",
                ),
                ReglaNormativa(
                    codigo="RG-PROMESA-02",
                    descripcion="No debe incluir promesas absolutas",
                    prohibido="garantizado",
                    severidad="media",
                ),
            ],
        )
    )
    bloqueo = evaluar_puerta_aprobacion_humana(
        SolicitudAprobacion(
            accion="publicar_comunicacion",
            descripcion="demo_v5",
            solicitante="cumplimiento",
            contexto={"origen": "verificacion_normativa"},
            aprobada=False,
        )
    )
    evidencia_2 = {
        "flujo": "normativa_y_bloqueo_humano",
        "pasos": [
            _serializar_resultado(verificacion),
            _serializar_resultado(bloqueo),
        ],
    }

    _guardar("demo_v5_integracion_riesgo_informe.json", evidencia_1)
    _guardar("demo_v5_integracion_normativa_aprobacion.json", evidencia_2)

    print(json.dumps({"evidencias_generadas": [evidencia_1["flujo"], evidencia_2["flujo"]]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
