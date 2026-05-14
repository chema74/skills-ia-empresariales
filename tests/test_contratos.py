from skillforge.core.contratos import ResultadoSkill


def test_resultado_skill_ok_y_trazabilidad_local() -> None:
    resultado = ResultadoSkill(
        nombre_skill="puerta_aprobacion_humana",
        estado="ok",
        salida={"mensaje": "Ejecución validada en entorno local"},
        trazas=["ejecucion_local: test_humo_v0"],
        advertencias=[],
    )

    assert resultado.es_correcto() is True
    assert "mensaje" in resultado.salida
    assert resultado.salida["mensaje"] == "Ejecución validada en entorno local"
    assert "ejecucion_local" in resultado.trazas[0]
