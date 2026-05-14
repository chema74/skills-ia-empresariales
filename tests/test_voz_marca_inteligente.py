from skillforge.skills import SolicitudVozMarca, evaluar_voz_marca_inteligente


def test_voz_marca_ok() -> None:
    entrada = SolicitudVozMarca(
        accion="adaptar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        texto="Actualizacion para clientes sobre soluciones disponibles.",
        tono_objetivo="ejecutivo",
        palabras_clave_marca=["clientes", "soluciones"],
    )

    resultado = evaluar_voz_marca_inteligente(entrada)

    assert resultado.estado == "ok"
    assert "Resumen ejecutivo" in resultado.salida["texto_adaptado"]
    assert resultado.salida["checklist_marca"]["incluye_palabras_clave"] is True


def test_voz_marca_error_texto_vacio() -> None:
    entrada = SolicitudVozMarca(
        accion="adaptar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        texto="",
    )

    resultado = evaluar_voz_marca_inteligente(entrada)

    assert resultado.estado == "error"
    assert "texto vacio" in resultado.salida["mensaje"].lower()