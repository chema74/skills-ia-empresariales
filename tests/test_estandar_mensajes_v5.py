from skillforge.skills import (
    SolicitudAprobacion,
    SolicitudForjadorInformes,
    SolicitudRadarAnomalias,
    evaluar_forjador_informes,
    evaluar_puerta_aprobacion_humana,
    evaluar_radar_anomalias,
)


def test_mensaje_ok_tiene_prefijo_estandar() -> None:
    resultado = evaluar_forjador_informes(
        SolicitudForjadorInformes(
            accion="forjar_informe",
            descripcion="v5",
            solicitante="qa",
            contexto={},
            hallazgos=["Hallazgo de prueba"],
        )
    )
    assert resultado.estado == "ok"
    assert resultado.salida["mensaje"].startswith("OK:")


def test_mensaje_error_tiene_prefijo_estandar() -> None:
    resultado = evaluar_radar_anomalias(
        SolicitudRadarAnomalias(
            accion="detectar_anomalias",
            descripcion="v5",
            solicitante="qa",
            contexto={},
            serie=[1, 2],
        )
    )
    assert resultado.estado == "error"
    assert resultado.salida["mensaje"].startswith("ERROR:")


def test_mensaje_advertencia_y_advertencias_normalizadas() -> None:
    resultado = evaluar_puerta_aprobacion_humana(
        SolicitudAprobacion(
            accion="aprobar_pago",
            descripcion="v5",
            solicitante="qa",
            contexto={},
            aprobada=False,
        )
    )
    assert resultado.estado == "advertencia"
    assert resultado.salida["mensaje"].startswith("ADVERTENCIA:")
    assert len(resultado.advertencias) >= 1
    assert all(advertencia.startswith("WARN:") for advertencia in resultado.advertencias)
