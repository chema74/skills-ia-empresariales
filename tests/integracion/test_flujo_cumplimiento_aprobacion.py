from skillforge.skills import (
    ReglaNormativa,
    SolicitudAprobacion,
    SolicitudForjadorInformes,
    SolicitudVerificacionNormativa,
    evaluar_forjador_informes,
    evaluar_puerta_aprobacion_humana,
    evaluar_verificador_normativo,
)


def test_flujo_integrado_cumplimiento_a_bloqueo_humano() -> None:
    verificacion = evaluar_verificador_normativo(
        SolicitudVerificacionNormativa(
            accion="verificar_normativa",
            descripcion="flujo_v5",
            solicitante="cumplimiento",
            contexto={},
            texto_objetivo="Comunicacion comercial sin consentimiento y con promesa garantizado.",
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

    assert verificacion.estado == "ok"
    assert verificacion.salida["total_no_conformidades"] >= 1
    assert verificacion.salida["severidad_global"] in {"media", "alta"}

    hallazgos = [f"No conformidades detectadas: {verificacion.salida['total_no_conformidades']}"]
    recomendaciones = [
        "Corregir texto comercial segun reglas normativas",
        "Enviar a revision legal antes de publicacion",
    ]
    informe = evaluar_forjador_informes(
        SolicitudForjadorInformes(
            accion="forjar_informe",
            descripcion="flujo_v5",
            solicitante="cumplimiento",
            contexto={},
            titulo="Informe de Cumplimiento Comercial",
            hallazgos=hallazgos,
            metricas={"no_conformidades": verificacion.salida["total_no_conformidades"]},
            recomendaciones=recomendaciones,
        )
    )

    assert informe.estado == "ok"
    assert "Informe de Cumplimiento Comercial" in informe.salida["informe_markdown"]

    aprobacion = evaluar_puerta_aprobacion_humana(
        SolicitudAprobacion(
            accion="publicar_comunicacion",
            descripcion="flujo_v5",
            solicitante="cumplimiento",
            contexto={"origen": "informe_cumplimiento"},
            aprobada=False,
        )
    )

    assert aprobacion.estado == "advertencia"
    assert aprobacion.salida["requiere_aprobador"] is True
