from skillforge.skills import SolicitudForjadorInformes, evaluar_forjador_informes


def test_forjador_informes_ok() -> None:
    entrada = SolicitudForjadorInformes(
        accion="forjar_informe",
        descripcion="test",
        solicitante="qa",
        contexto={},
        titulo="Informe QA",
        hallazgos=["Hallazgo 1"],
        metricas={"kpi": 10},
        recomendaciones=["Recomendacion 1"],
    )

    resultado = evaluar_forjador_informes(entrada)

    assert resultado.estado == "ok"
    assert resultado.es_correcto() is True
    assert "# Informe QA" in resultado.salida["informe_markdown"]


def test_forjador_informes_error_sin_datos() -> None:
    entrada = SolicitudForjadorInformes(
        accion="forjar_informe",
        descripcion="test",
        solicitante="qa",
        contexto={},
    )

    resultado = evaluar_forjador_informes(entrada)

    assert resultado.estado == "error"
    assert "no hay hallazgos" in resultado.salida["mensaje"].lower()