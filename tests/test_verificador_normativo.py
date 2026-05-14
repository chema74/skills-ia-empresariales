from skillforge.skills import ReglaNormativa, SolicitudVerificacionNormativa, evaluar_verificador_normativo


def test_verificador_normativo_ok_sin_incumplimientos() -> None:
    entrada = SolicitudVerificacionNormativa(
        accion="verificar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        texto_objetivo="Incluye trazabilidad y revisión humana.",
        reglas=[
            ReglaNormativa(codigo="R1", descripcion="req", requerido="trazabilidad", severidad="media"),
            ReglaNormativa(codigo="R2", descripcion="req", requerido="revisión humana", severidad="alta"),
        ],
    )

    resultado = evaluar_verificador_normativo(entrada)

    assert resultado.estado == "ok"
    assert resultado.salida["total_no_conformidades"] == 0


def test_verificador_normativo_detecta_no_conformidad() -> None:
    entrada = SolicitudVerificacionNormativa(
        accion="verificar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        texto_objetivo="Texto sin requisito.",
        reglas=[ReglaNormativa(codigo="R1", descripcion="req", requerido="trazabilidad", severidad="alta")],
    )

    resultado = evaluar_verificador_normativo(entrada)

    assert resultado.estado == "ok"
    assert resultado.salida["total_no_conformidades"] == 1
    assert resultado.salida["severidad_global"] == "alta"