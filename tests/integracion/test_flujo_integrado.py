from skillforge.skills import (
    FactorRiesgo,
    SolicitudEnrutamiento,
    SolicitudForjadorInformes,
    SolicitudPulsoRiesgo,
    evaluar_enrutador_inteligente,
    evaluar_forjador_informes,
    evaluar_pulso_riesgo,
)


def test_flujo_integrado_enrutado_riesgo_a_informe() -> None:
    enrutado = evaluar_enrutador_inteligente(
        SolicitudEnrutamiento(
            accion="enrutar",
            descripcion="flujo_integrado",
            solicitante="orquestador",
            contexto={"canal": "interno"},
            intencion="Necesito evaluar riesgo operativo y emitir informe",
        )
    )

    assert enrutado.estado == "ok"
    assert enrutado.salida["skill_destino"] in {"pulso_riesgo", "forjador_informes"}

    riesgo = evaluar_pulso_riesgo(
        SolicitudPulsoRiesgo(
            accion="calcular_riesgo",
            descripcion="flujo_integrado",
            solicitante="orquestador",
            contexto={},
            factores=[
                FactorRiesgo(nombre="continuidad", severidad=8, peso=4.0),
                FactorRiesgo(nombre="cumplimiento", severidad=7, peso=3.0),
            ],
            umbral_medio=20,
            umbral_alto=40,
        )
    )

    assert riesgo.estado == "ok"
    assert "nivel_riesgo" in riesgo.salida

    informe = evaluar_forjador_informes(
        SolicitudForjadorInformes(
            accion="forjar_informe",
            descripcion="flujo_integrado",
            solicitante="orquestador",
            contexto={},
            titulo="Informe Integrado Riesgo",
            hallazgos=[f"Nivel de riesgo detectado: {riesgo.salida['nivel_riesgo']}"],
            metricas={"puntuacion_riesgo": riesgo.salida["puntuacion"]},
            recomendaciones=riesgo.salida["recomendaciones"],
        )
    )

    assert informe.estado == "ok"
    assert "Informe Integrado Riesgo" in informe.salida["informe_markdown"]
    assert informe.salida["total_recomendaciones"] >= 1