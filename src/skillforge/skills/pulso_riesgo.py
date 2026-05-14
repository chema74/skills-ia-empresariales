"""Skill 05: Pulso de Riesgo (V1 local)."""

from dataclasses import dataclass, field

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


@dataclass
class FactorRiesgo:
    """Factor de riesgo con peso y severidad local."""

    nombre: str
    severidad: int
    peso: float


@dataclass
class SolicitudPulsoRiesgo(EntradaSkill):
    """Entrada para evaluar pulso de riesgo empresarial."""

    factores: list[FactorRiesgo] = field(default_factory=list)
    umbral_medio: float = 35.0
    umbral_alto: float = 70.0


class PulsoRiesgoSkill(SkillBase):
    """Calcula puntuacion de riesgo y recomendaciones por nivel."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="pulso_riesgo")

    def ejecutar(self, entrada: SolicitudPulsoRiesgo) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_pulso_riesgo")

        if not entrada.factores:
            self.nueva_traza(trazas, "sin_factores")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "No hay factores para evaluar riesgo"},
                trazas=trazas,
                advertencias=advertencias,
            )

        acumulado = 0.0
        detalle: list[dict[str, float | int | str]] = []
        for factor in entrada.factores:
            severidad = min(max(factor.severidad, 0), 10)
            if factor.severidad != severidad:
                advertencias.append(f"severidad ajustada a rango 0-10 en factor: {factor.nombre}")
            peso = max(factor.peso, 0.0)
            if factor.peso != peso:
                advertencias.append(f"peso negativo ajustado a 0 en factor: {factor.nombre}")

            contribucion = severidad * peso
            acumulado += contribucion
            detalle.append(
                {
                    "nombre": factor.nombre,
                    "severidad": severidad,
                    "peso": round(peso, 4),
                    "contribucion": round(contribucion, 4),
                }
            )

        self.nueva_traza(trazas, "puntuacion_calculada")
        puntuacion = round(acumulado, 4)

        if puntuacion >= entrada.umbral_alto:
            nivel = "alto"
            recomendaciones = [
                "Activar revisión humana prioritaria",
                "Aplicar plan de mitigación inmediato",
                "Escalar a comité de riesgo",
            ]
        elif puntuacion >= entrada.umbral_medio:
            nivel = "medio"
            recomendaciones = [
                "Programar revisión semanal de factores",
                "Definir acciones preventivas con responsables",
            ]
        else:
            nivel = "bajo"
            recomendaciones = [
                "Mantener monitoreo periódico",
                "Revalidar factores en el próximo ciclo",
            ]

        if entrada.umbral_medio >= entrada.umbral_alto:
            advertencias.append("umbral_medio debería ser menor que umbral_alto")

        self.nueva_traza(trazas, "clasificacion_riesgo")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Pulso de riesgo calculado en local",
                "puntuacion": puntuacion,
                "nivel_riesgo": nivel,
                "umbral_medio": entrada.umbral_medio,
                "umbral_alto": entrada.umbral_alto,
                "detalle_factores": detalle,
                "recomendaciones": recomendaciones,
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_pulso_riesgo(entrada: SolicitudPulsoRiesgo) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return PulsoRiesgoSkill().ejecutar(entrada)