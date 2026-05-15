"""Skill V2: Puerta de Aprobacion Humana."""

from dataclasses import dataclass

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.core.gobernanza import cargar_politicas, cargar_registro_cambios
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
    rol_aprobador: str | None = None
    evidencia_id: str | None = None
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

        accion = solicitud.accion.strip().lower()
        es_sensible = accion in ACCIONES_SENSIBLES
        politicas = cargar_politicas()
        politica = politicas.get(accion)
        version_politica = politica.version if politica else "legacy"
        registro_cambios = cargar_registro_cambios()

        if es_sensible and not solicitud.aprobada:
            advertencias.append("accion sensible bloqueada por falta de aprobacion humana")
            self.nueva_traza(trazas, "bloqueada_sin_aprobacion")
            return self.construir_resultado(
                estado="advertencia",
                salida={
                    "mensaje": "Accion bloqueada hasta revision humana",
                    "accion": accion,
                    "requiere_aprobador": True,
                    "gobernanza": {
                        "version_politica": version_politica,
                        "nivel_riesgo": politica.nivel_riesgo if politica else "no_definido",
                        "requiere_evidencia": politica.requiere_evidencia if politica else False,
                    },
                },
                trazas=trazas,
                advertencias=advertencias,
            )

        if es_sensible and solicitud.aprobada and politica:
            if not (solicitud.aprobador or "").strip():
                self.nueva_traza(trazas, "aprobacion_sin_aprobador")
                return self.construir_resultado(
                    estado="error",
                    salida={
                        "mensaje": "Aprobacion invalida: falta aprobador identificado",
                        "accion": accion,
                    },
                    trazas=trazas,
                    advertencias=advertencias,
                )

            rol_aprobador = (solicitud.rol_aprobador or "").strip().lower()
            if politica.roles_aprobadores and rol_aprobador not in politica.roles_aprobadores:
                self.nueva_traza(trazas, "rol_aprobador_no_autorizado")
                return self.construir_resultado(
                    estado="error",
                    salida={
                        "mensaje": "Aprobacion invalida: rol_aprobador no autorizado por politica",
                        "accion": accion,
                        "roles_permitidos": politica.roles_aprobadores,
                    },
                    trazas=trazas,
                    advertencias=advertencias,
                )

            if politica.requiere_evidencia and not (solicitud.evidencia_id or "").strip():
                self.nueva_traza(trazas, "falta_evidencia_aprobacion")
                return self.construir_resultado(
                    estado="error",
                    salida={
                        "mensaje": "Aprobacion invalida: falta evidencia para accion sensible",
                        "accion": accion,
                    },
                    trazas=trazas,
                    advertencias=advertencias,
                )

        self.nueva_traza(trazas, "aprobada_para_ejecucion")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Accion habilitada con control humano",
                "accion": accion,
                "aprobador": solicitud.aprobador,
                "rol_aprobador": solicitud.rol_aprobador,
                "evidencia_id": solicitud.evidencia_id,
                "gobernanza": {
                    "version_politica": version_politica,
                    "nivel_riesgo": politica.nivel_riesgo if politica else "no_definido",
                    "roles_permitidos": politica.roles_aprobadores if politica else [],
                    "registro_cambios_total": len(registro_cambios),
                },
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_puerta_aprobacion_humana(solicitud: SolicitudAprobacion) -> ResultadoSkill:
    """Compatibilidad con API funcional previa."""

    return PuertaAprobacionHumanaSkill().evaluar(solicitud)
