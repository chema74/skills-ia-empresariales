from skillforge.core.contratos import ResultadoSkill
from skillforge.core.validacion import validar_resultado_skill


def test_validar_resultado_skill_ok() -> None:
    resultado = ResultadoSkill(
        nombre_skill="puerta_aprobacion_humana",
        estado="ok",
        salida={"mensaje": "Resultado correcto"},
        trazas=["ejecucion_local: v1"],
        advertencias=[],
    )

    es_valido, errores = validar_resultado_skill(resultado)

    assert es_valido is True
    assert errores == []


def test_validar_resultado_skill_con_errores() -> None:
    resultado = ResultadoSkill(
        nombre_skill="",
        estado="desconocido",
        salida={},
        trazas=[],
        advertencias=[],
    )

    es_valido, errores = validar_resultado_skill(resultado)

    assert es_valido is False
    assert len(errores) == 4