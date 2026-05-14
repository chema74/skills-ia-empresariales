from skillforge.skills import SolicitudEnrutamiento, evaluar_enrutador_inteligente


def test_enrutador_ruta_unica() -> None:
    entrada = SolicitudEnrutamiento(
        accion="enrutar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        intencion="Necesito revisar riesgo operativo",
    )

    resultado = evaluar_enrutador_inteligente(entrada)

    assert resultado.estado == "ok"
    assert resultado.salida["skill_destino"] == "pulso_riesgo"


def test_enrutador_ambiguedad() -> None:
    entrada = SolicitudEnrutamiento(
        accion="enrutar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        intencion="Detectar anomalia y crear informe",
    )

    resultado = evaluar_enrutador_inteligente(entrada)

    assert resultado.estado == "ok"
    assert len(resultado.salida["skills_candidatas"]) >= 2
    assert any("ambigua" in a for a in resultado.advertencias)


def test_enrutador_sin_coincidencias() -> None:
    entrada = SolicitudEnrutamiento(
        accion="enrutar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        intencion="Tema no reconocido",
    )

    resultado = evaluar_enrutador_inteligente(entrada)

    assert resultado.estado == "ok"
    assert resultado.salida["skill_destino"] == "revision_humana"