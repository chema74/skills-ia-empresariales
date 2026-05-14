from skillforge.core.contratos import EntradaSkill


def test_entrada_skill_basica() -> None:
    entrada = EntradaSkill(
        accion="aprobar_pago",
        descripcion="Pago mensual",
        solicitante="finanzas",
        contexto={"area": "compras"},
    )

    assert entrada.accion == "aprobar_pago"
    assert entrada.contexto["area"] == "compras"