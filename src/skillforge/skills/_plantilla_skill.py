"""Plantilla oficial para acelerar nuevas skills empresariales."""

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


class PlantillaSkill(SkillBase):
    """Blueprint para implementar una skill con contrato comun."""

    def __init__(self, nombre_skill: str = "plantilla_skill") -> None:
        super().__init__(nombre_skill=nombre_skill)

    def ejecutar(self, entrada: EntradaSkill) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []

        self.nueva_traza(trazas, "inicio_ejecucion")

        if not entrada.accion.strip() or not entrada.descripcion.strip() or not entrada.solicitante.strip():
            self.nueva_traza(trazas, "entrada_invalida")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Entrada invalida: faltan campos obligatorios"},
                trazas=trazas,
                advertencias=advertencias,
            )

        self.nueva_traza(trazas, "ejecucion_local_ok")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Plantilla ejecutada correctamente",
                "accion": entrada.accion,
                "solicitante": entrada.solicitante,
                "contexto": entrada.contexto,
            },
            trazas=trazas,
            advertencias=advertencias,
        )