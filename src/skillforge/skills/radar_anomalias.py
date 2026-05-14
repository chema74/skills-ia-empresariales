"""Skill 02: Radar de Anomalias (V1 local)."""

from dataclasses import dataclass, field
from statistics import mean, pstdev

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


@dataclass
class SolicitudRadarAnomalias(EntradaSkill):
    """Entrada para deteccion local de anomalias numericas."""

    serie: list[float] = field(default_factory=list)
    umbral_desviaciones: float = 2.0


class RadarAnomaliasSkill(SkillBase):
    """Detecta valores atipicos sobre una serie numerica."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="radar_anomalias")

    def ejecutar(self, entrada: SolicitudRadarAnomalias) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_radar_anomalias")

        if len(entrada.serie) < 3:
            self.nueva_traza(trazas, "serie_insuficiente")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Serie insuficiente: se requieren al menos 3 valores"},
                trazas=trazas,
                advertencias=advertencias,
            )

        media = mean(entrada.serie)
        desv = pstdev(entrada.serie)
        self.nueva_traza(trazas, "estadisticas_calculadas")

        if desv == 0:
            advertencias.append("serie sin variacion: no hay anomalias estadisticas")
            self.nueva_traza(trazas, "sin_variacion")
            return self.construir_resultado(
                estado="ok",
                salida={
                    "mensaje": "Analisis completado sin variacion",
                    "media": media,
                    "desviacion": desv,
                    "anomalias": [],
                },
                trazas=trazas,
                advertencias=advertencias,
            )

        anomalias: list[dict[str, float | int]] = []
        umbral = entrada.umbral_desviaciones
        for idx, valor in enumerate(entrada.serie):
            z = abs((valor - media) / desv)
            if z >= umbral:
                anomalias.append({"indice": idx, "valor": valor, "z_score": round(z, 4)})

        if not anomalias:
            advertencias.append("no se detectaron anomalias con el umbral actual")

        self.nueva_traza(trazas, "deteccion_finalizada")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Radar de anomalias completado en local",
                "media": round(media, 4),
                "desviacion": round(desv, 4),
                "umbral_desviaciones": umbral,
                "total_anomalias": len(anomalias),
                "anomalias": anomalias,
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_radar_anomalias(entrada: SolicitudRadarAnomalias) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return RadarAnomaliasSkill().ejecutar(entrada)