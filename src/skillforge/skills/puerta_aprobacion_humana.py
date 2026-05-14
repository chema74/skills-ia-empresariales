"""Skill V2: Puerta de Aprobacion Humana."""

from dataclasses import dataclass

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


ACCIONES_SENSIBLES = {
    "enviar_correo_externo",
    "aprobar_pago",
    "modificar_contrato",
    "publicar_comunicacion",
}


@dataclass
class SolicitudAprobacion(EntradaSkill):
    """Solicitud de accion que requiere control humano."""

    aprobador: str | None = None
    aprobada: bool = False


class PuertaAprobacionHumanaSkill(SkillBase):
    """Skill de control humano para acciones sensibles."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="puerta_aprobacion_humana")

    def evaluar(self, solicitud: SolicitudAprobacion) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []

        self.nueva_traza(trazas, "inicio_evaluacion")

        if not solicitud.accion.strip() or not solicitud.descripcion.strip() or not solicitud.solicitante.strip():
            self.nueva_traza(trazas, "entrada_invalida")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Solicitud invalida: faltan campos obligatorios"},
                trazas=trazas,
                advertencias=advertencias,
            )

        es_sensible = solicitud.accion in ACCIONES_SENSIBLES
        if es_sensible and not solicitud.aprobada:
            advertencias.append("accion sensible bloqueada por falta de aprobacion humana")
            self.nueva_traza(trazas, "bloqueada_sin_aprobacion")
            return self.construir_resultado(
                estado="advertencia",
                salida={
                    "mensaje": "Accion bloqueada hasta revision humana",
                    "accion": solicitud.accion,
                    "requiere_aprobador": True,
                },
                trazas=trazas,
                advertencias=advertencias,
            )

        self.nueva_traza(trazas, "aprobada_para_ejecucion")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Accion habilitada con control humano",
                "accion": solicitud.accion,
                "aprobador": solicitud.aprobador,
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_puerta_aprobacion_humana(solicitud: SolicitudAprobacion) -> ResultadoSkill:
    """Compatibilidad con API funcional previa."""

    return PuertaAprobacionHumanaSkill().evaluar(solicitud)