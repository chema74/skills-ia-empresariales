from skillforge.skills import SolicitudLecturaDocumental, evaluar_lector_inteligente_documental


def test_lector_documental_ok() -> None:
    entrada = SolicitudLecturaDocumental(
        accion="leer_documento",
        descripcion="test",
        solicitante="qa",
        contexto={"caso": "ok"},
        texto_documento="Titulo\n\nRiesgo operativo detectado\n\nAccion: ajustar presupuesto",
        palabras_clave=["riesgo", "presupuesto"],
    )

    resultado = evaluar_lector_inteligente_documental(entrada)

    assert resultado.estado == "ok"
    assert resultado.es_correcto() is True
    assert resultado.salida["total_secciones"] >= 1
    assert "riesgo" in resultado.salida["palabras_detectadas"]


def test_lector_documental_error_documento_vacio() -> None:
    entrada = SolicitudLecturaDocumental(
        accion="leer_documento",
        descripcion="test",
        solicitante="qa",
        contexto={},
        texto_documento="",
    )

    resultado = evaluar_lector_inteligente_documental(entrada)

    assert resultado.estado == "error"
    assert "vacio" in resultado.salida["mensaje"].lower()