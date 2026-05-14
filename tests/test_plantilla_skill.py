from skillforge.core.contratos import EntradaSkill
from skillforge.skills._plantilla_skill import PlantillaSkill


def test_plantilla_skill_ok() -> None:
    skill = PlantillaSkill(nombre_skill="plantilla_demo")
    entrada = EntradaSkill(
        accion="procesar",
        descripcion="Prueba local",
        solicitante="qa",
        contexto={"origen": "test"},
    )

    resultado = skill.ejecutar(entrada)

    assert resultado.estado == "ok"
    assert resultado.es_correcto() is True
    assert resultado.salida["accion"] == "procesar"


def test_plantilla_skill_error_en_entrada_vacia() -> None:
    skill = PlantillaSkill()
    entrada = EntradaSkill(accion="", descripcion="", solicitante="")

    resultado = skill.ejecutar(entrada)

    assert resultado.estado == "error"
    assert "invalida" in resultado.salida["mensaje"].lower()