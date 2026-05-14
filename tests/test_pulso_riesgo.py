from skillforge.skills import FactorRiesgo, SolicitudPulsoRiesgo, evaluar_pulso_riesgo


def test_pulso_riesgo_nivel_alto() -> None:
    entrada = SolicitudPulsoRiesgo(
        accion="calcular",
        descripcion="test",
        solicitante="qa",
        contexto={},
        factores=[
            FactorRiesgo(nombre="f1", severidad=10, peso=5.0),
            FactorRiesgo(nombre="f2", severidad=8, peso=4.0),
        ],
        umbral_medio=20,
        umbral_alto=40,
    )

    resultado = evaluar_pulso_riesgo(entrada)

    assert resultado.estado == "ok"
    assert resultado.salida["nivel_riesgo"] == "alto"


def test_pulso_riesgo_error_sin_factores() -> None:
    entrada = SolicitudPulsoRiesgo(
        accion="calcular",
        descripcion="test",
        solicitante="qa",
        contexto={},
        factores=[],
    )

    resultado = evaluar_pulso_riesgo(entrada)

    assert resultado.estado == "error"
    assert "no hay factores" in resultado.salida["mensaje"].lower()


def test_pulso_riesgo_ajustes_y_advertencias() -> None:
    entrada = SolicitudPulsoRiesgo(
        accion="calcular",
        descripcion="test",
        solicitante="qa",
        contexto={},
        factores=[FactorRiesgo(nombre="f", severidad=99, peso=-2.0)],
        umbral_medio=100,
        umbral_alto=50,
    )

    resultado = evaluar_pulso_riesgo(entrada)

    assert resultado.estado == "ok"
    assert any("severidad ajustada" in a for a in resultado.advertencias)
    assert any("umbral_medio" in a for a in resultado.advertencias)