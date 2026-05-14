"""Skill V2: Puerta de Aprobacion Humana."""

from dataclasses import dataclass

from skillforge.core.contratos import ResultadoSkill
from skillforge.core.trazabilidad import agregar_traza_local
from skillforge.core.validacion import validar_resultado_skill


ACCIONES_SENSIBLES = {
    "enviar_correo_externo",
    "aprobar_pago",
    "modificar_contrato",
    "publicar_comunicacion",
}


@dataclass
class SolicitudAprobacion:
    """Solicitud de accion que requiere control humano."""

    accion: str
    descripcion: str
    solicitante: str
    aprobador: str | None = None
    aprobada: bool = False


def evaluar_puerta_aprobacion_humana(solicitud: SolicitudAprobacion) -> ResultadoSkill:
    """Evalua una solicitud y registra decision con trazabilidad local."""

    trazas: list[str] = []
    advertencias: list[str] = []

    agregar_traza_local(trazas, "inicio_evaluacion")

    if not solicitud.accion.strip() or not solicitud.descripcion.strip() or not solicitud.solicitante.strip():
        agregar_traza_local(trazas, "entrada_invalida")
        resultado = ResultadoSkill(
            nombre_skill="puerta_aprobacion_humana",
            estado="error",
            salida={"mensaje": "Solicitud invalida: faltan campos obligatorios"},
            trazas=trazas,
            advertencias=advertencias,
        )
        return resultado

    es_sensible = solicitud.accion in ACCIONES_SENSIBLES

    if es_sensible and not solicitud.aprobada:
        advertencias.append("accion sensible bloqueada por falta de aprobacion humana")
        agregar_traza_local(trazas, "bloqueada_sin_aprobacion")
        resultado = ResultadoSkill(
            nombre_skill="puerta_aprobacion_humana",
            estado="advertencia",
            salida={
                "mensaje": "Accion bloqueada hasta revision humana",
                "accion": solicitud.accion,
                "requiere_aprobador": True,
            },
            trazas=trazas,
            advertencias=advertencias,
        )
    else:
        agregar_traza_local(trazas, "aprobada_para_ejecucion")
        resultado = ResultadoSkill(
            nombre_skill="puerta_aprobacion_humana",
            estado="ok",
            salida={
                "mensaje": "Accion habilitada con control humano",
                "accion": solicitud.accion,
                "aprobador": solicitud.aprobador,
            },
            trazas=trazas,
            advertencias=advertencias,
        )

    es_valido, errores = validar_resultado_skill(resultado)
    if not es_valido:
        agregar_traza_local(trazas, "resultado_con_errores_de_contrato")
        resultado.estado = "error"
        resultado.advertencias.extend(errores)
        resultado.salida["mensaje"] = "Resultado invalido por reglas de contrato"

    return resultado