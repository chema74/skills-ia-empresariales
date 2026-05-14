"""Skill 03: Forjador de Informes (V1 local)."""

from dataclasses import dataclass, field

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


@dataclass
class SolicitudForjadorInformes(EntradaSkill):
    """Entrada para construir informes ejecutivos locales."""

    titulo: str = "Informe Empresarial"
    hallazgos: list[str] = field(default_factory=list)
    metricas: dict[str, float | int | str] = field(default_factory=dict)
    recomendaciones: list[str] = field(default_factory=list)


class ForjadorInformesSkill(SkillBase):
    """Construye un informe estructurado en texto markdown."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="forjador_informes")

    def ejecutar(self, entrada: SolicitudForjadorInformes) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_forjado_informe")

        if not entrada.hallazgos and not entrada.metricas:
            self.nueva_traza(trazas, "entrada_sin_contenido")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "No hay hallazgos ni metricas para construir el informe"},
                trazas=trazas,
                advertencias=advertencias,
            )

        seccion_metricas = "\n".join([f"- {k}: {v}" for k, v in entrada.metricas.items()]) or "- Sin metricas"
        seccion_hallazgos = "\n".join([f"- {h}" for h in entrada.hallazgos]) or "- Sin hallazgos"
        seccion_recomendaciones = (
            "\n".join([f"- {r}" for r in entrada.recomendaciones]) or "- Sin recomendaciones"
        )

        informe_md = (
            f"# {entrada.titulo}\n\n"
            f"## Contexto\n"
            f"Solicitante: {entrada.solicitante}\n"
            f"Descripcion: {entrada.descripcion}\n\n"
            f"## Metricas\n{seccion_metricas}\n\n"
            f"## Hallazgos\n{seccion_hallazgos}\n\n"
            f"## Recomendaciones\n{seccion_recomendaciones}\n"
        )

        if not entrada.recomendaciones:
            advertencias.append("informe sin recomendaciones explicitas")

        self.nueva_traza(trazas, "informe_generado")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Informe generado en local",
                "titulo": entrada.titulo,
                "informe_markdown": informe_md,
                "total_hallazgos": len(entrada.hallazgos),
                "total_metricas": len(entrada.metricas),
                "total_recomendaciones": len(entrada.recomendaciones),
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_forjador_informes(entrada: SolicitudForjadorInformes) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return ForjadorInformesSkill().ejecutar(entrada)