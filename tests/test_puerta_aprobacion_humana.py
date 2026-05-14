from skillforge.skills import SolicitudAprobacion, evaluar_puerta_aprobacion_humana


def test_bloquea_accion_sensible_sin_aprobacion() -> None:
    solicitud = SolicitudAprobacion(
        accion="aprobar_pago",
        descripcion="Pago extraordinario",
        solicitante="finanzas",
        aprobada=False,
    )

    resultado = evaluar_puerta_aprobacion_humana(solicitud)

    assert resultado.estado == "advertencia"
    assert resultado.es_correcto() is False
    assert resultado.salida["requiere_aprobador"] is True
    assert any("bloqueada" in traza for traza in resultado.trazas)


def test_habilita_accion_sensible_con_aprobacion() -> None:
    solicitud = SolicitudAprobacion(
        accion="aprobar_pago",
        descripcion="Pago extraordinario",
        solicitante="finanzas",
        aprobador="direccion",
        aprobada=True,
    )

    resultado = evaluar_puerta_aprobacion_humana(solicitud)

    assert resultado.estado == "ok"
    assert resultado.es_correcto() is True
    assert resultado.salida["aprobador"] == "direccion"


def test_error_si_faltan_campos_obligatorios() -> None:
    solicitud = SolicitudAprobacion(
        accion="",
        descripcion="",
        solicitante="",
    )

    resultado = evaluar_puerta_aprobacion_humana(solicitud)

    assert resultado.estado == "error"
    assert "invalida" in resultado.salida["mensaje"].lower()