from skillforge.skills import SolicitudRadarAnomalias, evaluar_radar_anomalias


def test_radar_anomalias_detecta_valor_atipico() -> None:
    entrada = SolicitudRadarAnomalias(
        accion="detectar_anomalias",
        descripcion="test",
        solicitante="qa",
        contexto={},
        serie=[10, 11, 10, 12, 100, 11],
        umbral_desviaciones=1.8,
    )

    resultado = evaluar_radar_anomalias(entrada)

    assert resultado.estado == "ok"
    assert resultado.es_correcto() is True
    assert resultado.salida["total_anomalias"] >= 1


def test_radar_anomalias_error_serie_corta() -> None:
    entrada = SolicitudRadarAnomalias(
        accion="detectar_anomalias",
        descripcion="test",
        solicitante="qa",
        contexto={},
        serie=[1, 2],
    )

    resultado = evaluar_radar_anomalias(entrada)

    assert resultado.estado == "error"
    assert "insuficiente" in resultado.salida["mensaje"].lower()


def test_radar_anomalias_sin_variacion() -> None:
    entrada = SolicitudRadarAnomalias(
        accion="detectar_anomalias",
        descripcion="test",
        solicitante="qa",
        contexto={},
        serie=[5, 5, 5, 5],
    )

    resultado = evaluar_radar_anomalias(entrada)

    assert resultado.estado == "ok"
    assert resultado.salida["anomalias"] == []
    assert any("sin variacion" in a for a in resultado.advertencias)