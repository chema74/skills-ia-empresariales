"""Skill 09: Verificador Normativo (V1 local)."""

from dataclasses import dataclass, field

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


@dataclass
class ReglaNormativa:
    """Regla local de cumplimiento documental."""

    codigo: str
    descripcion: str
    requerido: str | None = None
    prohibido: str | None = None
    severidad: str = "media"


@dataclass
class SolicitudVerificacionNormativa(EntradaSkill):
    """Entrada para verificación local de cumplimiento."""

    texto_objetivo: str = ""
    reglas: list[ReglaNormativa] = field(default_factory=list)


class VerificadorNormativoSkill(SkillBase):
    """Evalúa texto contra reglas normativas internas."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="verificador_normativo")

    def ejecutar(self, entrada: SolicitudVerificacionNormativa) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_verificacion_normativa")

        if not entrada.texto_objetivo.strip():
            self.nueva_traza(trazas, "texto_objetivo_vacio")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Texto objetivo vacio"},
                trazas=trazas,
                advertencias=advertencias,
            )

        if not entrada.reglas:
            self.nueva_traza(trazas, "sin_reglas")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "No hay reglas normativas definidas"},
                trazas=trazas,
                advertencias=advertencias,
            )

        txt = entrada.texto_objetivo.lower()
        no_conformidades: list[dict[str, str]] = []
        conformidades: list[str] = []

        for r in entrada.reglas:
            incumple = False
            motivo = ""
            if r.requerido and r.requerido.lower() not in txt:
                incumple = True
                motivo = f"falta requerido: {r.requerido}"
            if r.prohibido and r.prohibido.lower() in txt:
                incumple = True
                motivo = f"contiene prohibido: {r.prohibido}"

            if incumple:
                no_conformidades.append(
                    {
                        "codigo": r.codigo,
                        "descripcion": r.descripcion,
                        "severidad": r.severidad,
                        "motivo": motivo,
                    }
                )
            else:
                conformidades.append(r.codigo)

        self.nueva_traza(trazas, "reglas_evaluadas")

        severidad_global = "baja"
        if any(nc["severidad"] == "alta" for nc in no_conformidades):
            severidad_global = "alta"
        elif any(nc["severidad"] == "media" for nc in no_conformidades):
            severidad_global = "media"

        if no_conformidades:
            advertencias.append("se detectan no conformidades: requiere revision humana")

        self.nueva_traza(trazas, "informe_normativo_generado")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Verificacion normativa completada en local",
                "total_reglas": len(entrada.reglas),
                "total_conformidades": len(conformidades),
                "total_no_conformidades": len(no_conformidades),
                "severidad_global": severidad_global,
                "conformidades": conformidades,
                "no_conformidades": no_conformidades,
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_verificador_normativo(entrada: SolicitudVerificacionNormativa) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return VerificadorNormativoSkill().ejecutar(entrada)