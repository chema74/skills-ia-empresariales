"""Skill V6: Orquestador Multi-skill local con pipelines empresariales."""

from dataclasses import dataclass, field
from typing import Any

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase
from skillforge.skills.enrutador_inteligente import SolicitudEnrutamiento, evaluar_enrutador_inteligente
from skillforge.skills.forjador_informes import SolicitudForjadorInformes, evaluar_forjador_informes
from skillforge.skills.memoria_contextual_cliente import (
    EventoCliente,
    SolicitudMemoriaCliente,
    evaluar_memoria_contextual_cliente,
)
from skillforge.skills.puerta_aprobacion_humana import SolicitudAprobacion, evaluar_puerta_aprobacion_humana
from skillforge.skills.pulso_riesgo import FactorRiesgo, SolicitudPulsoRiesgo, evaluar_pulso_riesgo
from skillforge.skills.verificador_normativo import (
    ReglaNormativa,
    SolicitudVerificacionNormativa,
    evaluar_verificador_normativo,
)
from skillforge.skills.voz_marca_inteligente import SolicitudVozMarca, evaluar_voz_marca_inteligente


PIPELINE_RIESGO_INFORME = "riesgo_informe"
PIPELINE_CUMPLIMIENTO_PUBLICACION = "cumplimiento_publicacion"
PIPELINE_CLIENTE_COMUNICACION = "cliente_comunicacion"

PIPELINES_DISPONIBLES = {
    PIPELINE_RIESGO_INFORME,
    PIPELINE_CUMPLIMIENTO_PUBLICACION,
    PIPELINE_CLIENTE_COMUNICACION,
}


@dataclass
class SolicitudOrquestacion(EntradaSkill):
    """Entrada para ejecutar un pipeline multi-skill."""

    pipeline_id: str = ""
    entrada_pipeline: dict[str, Any] = field(default_factory=dict)


class OrquestadorMultiSkill(SkillBase):
    """Orquesta pipelines de negocio con trazabilidad de extremo a extremo."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="orquestador_multiskill")

    def ejecutar(self, entrada: SolicitudOrquestacion) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, f"inicio_pipeline:{entrada.pipeline_id or 'sin_id'}")

        pipeline_id = entrada.pipeline_id.strip().lower()
        if pipeline_id not in PIPELINES_DISPONIBLES:
            self.nueva_traza(trazas, "pipeline_no_soportado")
            return self.construir_resultado(
                estado="error",
                salida={
                    "mensaje": f"Pipeline no soportado: {pipeline_id or 'vacio'}",
                    "pipelines_disponibles": sorted(PIPELINES_DISPONIBLES),
                },
                trazas=trazas,
                advertencias=advertencias,
            )

        if pipeline_id == PIPELINE_RIESGO_INFORME:
            pasos = self._pipeline_riesgo_informe(entrada, trazas, advertencias)
        elif pipeline_id == PIPELINE_CUMPLIMIENTO_PUBLICACION:
            pasos = self._pipeline_cumplimiento_publicacion(entrada, trazas, advertencias)
        else:
            pasos = self._pipeline_cliente_comunicacion(entrada, trazas, advertencias)

        estados_pasos = [paso["estado"] for paso in pasos]
        if any(estado == "error" for estado in estados_pasos):
            estado_final = "error"
        elif any(estado == "advertencia" for estado in estados_pasos):
            estado_final = "advertencia"
        else:
            estado_final = "ok"

        self.nueva_traza(trazas, f"fin_pipeline:{pipeline_id}:estado={estado_final}")
        return self.construir_resultado(
            estado=estado_final,
            salida={
                "mensaje": f"Pipeline ejecutado: {pipeline_id}",
                "pipeline_id": pipeline_id,
                "total_pasos": len(pasos),
                "pasos": pasos,
            },
            trazas=trazas,
            advertencias=advertencias,
        )

    def _pipeline_riesgo_informe(
        self,
        entrada: SolicitudOrquestacion,
        trazas: list[str],
        advertencias: list[str],
    ) -> list[dict[str, Any]]:
        data = entrada.entrada_pipeline
        intencion = str(data.get("intencion", "Necesito evaluar riesgo y generar informe"))
        factores_data = data.get("factores", [])
        factores = [
            FactorRiesgo(
                nombre=str(factor.get("nombre", "sin_nombre")),
                severidad=int(factor.get("severidad", 0)),
                peso=float(factor.get("peso", 0.0)),
            )
            for factor in factores_data
            if isinstance(factor, dict)
        ]
        if not factores:
            advertencias.append("pipeline riesgo_informe sin factores, se usa factor por defecto")
            factores = [FactorRiesgo(nombre="operativo", severidad=5, peso=2.0)]

        pasos: list[dict[str, Any]] = []
        self.nueva_traza(trazas, "pipeline:riesgo_informe:paso:enrutamiento:inicio")
        enrutado = evaluar_enrutador_inteligente(
            SolicitudEnrutamiento(
                accion="enrutar",
                descripcion=entrada.descripcion,
                solicitante=entrada.solicitante,
                contexto=entrada.contexto,
                intencion=intencion,
            )
        )
        pasos.append(self._serializar_paso("enrutamiento", enrutado))
        trazas.extend([f"paso:enrutamiento:{traza}" for traza in enrutado.trazas])
        advertencias.extend(enrutado.advertencias)

        self.nueva_traza(trazas, "pipeline:riesgo_informe:paso:pulso_riesgo:inicio")
        riesgo = evaluar_pulso_riesgo(
            SolicitudPulsoRiesgo(
                accion="calcular_riesgo",
                descripcion=entrada.descripcion,
                solicitante=entrada.solicitante,
                contexto=entrada.contexto,
                factores=factores,
            )
        )
        pasos.append(self._serializar_paso("pulso_riesgo", riesgo))
        trazas.extend([f"paso:pulso_riesgo:{traza}" for traza in riesgo.trazas])
        advertencias.extend(riesgo.advertencias)

        self.nueva_traza(trazas, "pipeline:riesgo_informe:paso:forjador_informes:inicio")
        informe = evaluar_forjador_informes(
            SolicitudForjadorInformes(
                accion="forjar_informe",
                descripcion=entrada.descripcion,
                solicitante=entrada.solicitante,
                contexto=entrada.contexto,
                titulo=str(data.get("titulo", "Informe Integrado de Riesgo")),
                hallazgos=[f"Nivel de riesgo: {riesgo.salida.get('nivel_riesgo', 'desconocido')}"],
                metricas={"puntuacion_riesgo": riesgo.salida.get("puntuacion", 0)},
                recomendaciones=list(riesgo.salida.get("recomendaciones", [])),
            )
        )
        pasos.append(self._serializar_paso("forjador_informes", informe))
        trazas.extend([f"paso:forjador_informes:{traza}" for traza in informe.trazas])
        advertencias.extend(informe.advertencias)

        return pasos

    def _pipeline_cumplimiento_publicacion(
        self,
        entrada: SolicitudOrquestacion,
        trazas: list[str],
        advertencias: list[str],
    ) -> list[dict[str, Any]]:
        data = entrada.entrada_pipeline
        texto_objetivo = str(data.get("texto_objetivo", "Comunicacion sin consentimiento."))
        reglas_data = data.get("reglas", [])
        reglas = [
            ReglaNormativa(
                codigo=str(regla.get("codigo", "RG-SIN-CODIGO")),
                descripcion=str(regla.get("descripcion", "Regla generica")),
                requerido=regla.get("requerido"),
                prohibido=regla.get("prohibido"),
                severidad=str(regla.get("severidad", "media")),
            )
            for regla in reglas_data
            if isinstance(regla, dict)
        ]
        if not reglas:
            advertencias.append("pipeline cumplimiento_publicacion sin reglas, se usa regla por defecto")
            reglas = [
                ReglaNormativa(
                    codigo="RG-CONSENT",
                    descripcion="Debe incluir consentimiento",
                    requerido="consentimiento",
                    severidad="alta",
                )
            ]

        pasos: list[dict[str, Any]] = []
        self.nueva_traza(trazas, "pipeline:cumplimiento_publicacion:paso:verificador_normativo:inicio")
        verificacion = evaluar_verificador_normativo(
            SolicitudVerificacionNormativa(
                accion="verificar_normativa",
                descripcion=entrada.descripcion,
                solicitante=entrada.solicitante,
                contexto=entrada.contexto,
                texto_objetivo=texto_objetivo,
                reglas=reglas,
            )
        )
        pasos.append(self._serializar_paso("verificador_normativo", verificacion))
        trazas.extend([f"paso:verificador_normativo:{traza}" for traza in verificacion.trazas])
        advertencias.extend(verificacion.advertencias)

        requiere_aprobacion = verificacion.salida.get("total_no_conformidades", 0) > 0
        self.nueva_traza(trazas, "pipeline:cumplimiento_publicacion:paso:puerta_aprobacion_humana:inicio")
        aprobacion = evaluar_puerta_aprobacion_humana(
            SolicitudAprobacion(
                accion="publicar_comunicacion",
                descripcion=entrada.descripcion,
                solicitante=entrada.solicitante,
                contexto=entrada.contexto,
                aprobada=not requiere_aprobacion,
                aprobador=data.get("aprobador") if not requiere_aprobacion else None,
            )
        )
        pasos.append(self._serializar_paso("puerta_aprobacion_humana", aprobacion))
        trazas.extend([f"paso:puerta_aprobacion_humana:{traza}" for traza in aprobacion.trazas])
        advertencias.extend(aprobacion.advertencias)

        return pasos

    def _pipeline_cliente_comunicacion(
        self,
        entrada: SolicitudOrquestacion,
        trazas: list[str],
        advertencias: list[str],
    ) -> list[dict[str, Any]]:
        data = entrada.entrada_pipeline
        cliente_id = str(data.get("cliente_id", "CLI-GENERICO"))
        eventos_data = data.get("eventos", [])
        eventos = [
            EventoCliente(
                fecha=str(evento.get("fecha", "2026-01-01T00:00:00")),
                tipo=str(evento.get("tipo", "contacto")),
                detalle=str(evento.get("detalle", "sin detalle")),
                origen=str(evento.get("origen", "origen_desconocido")),
            )
            for evento in eventos_data
            if isinstance(evento, dict)
        ]
        if not eventos:
            advertencias.append("pipeline cliente_comunicacion sin eventos, se usa evento por defecto")
            eventos = [
                EventoCliente(
                    fecha="2026-01-01T09:00:00",
                    tipo="contacto",
                    detalle="contacto inicial",
                    origen="crm",
                )
            ]

        pasos: list[dict[str, Any]] = []
        self.nueva_traza(trazas, "pipeline:cliente_comunicacion:paso:memoria_contextual_cliente:inicio")
        memoria = evaluar_memoria_contextual_cliente(
            SolicitudMemoriaCliente(
                accion="consolidar_memoria",
                descripcion=entrada.descripcion,
                solicitante=entrada.solicitante,
                contexto=entrada.contexto,
                cliente_id=cliente_id,
                eventos=eventos,
                responsable_actual=data.get("responsable_actual"),
                prioridad_actual=data.get("prioridad_actual"),
            )
        )
        pasos.append(self._serializar_paso("memoria_contextual_cliente", memoria))
        trazas.extend([f"paso:memoria_contextual_cliente:{traza}" for traza in memoria.trazas])
        advertencias.extend(memoria.advertencias)

        resumen_cliente = memoria.salida.get("ultima_interaccion", {})
        texto_base = (
            f"Cliente {cliente_id}. Ultima interaccion: "
            f"{resumen_cliente.get('tipo', 'sin tipo')} - {resumen_cliente.get('detalle', 'sin detalle')}."
        )
        self.nueva_traza(trazas, "pipeline:cliente_comunicacion:paso:voz_marca_inteligente:inicio")
        voz = evaluar_voz_marca_inteligente(
            SolicitudVozMarca(
                accion="adaptar_texto",
                descripcion=entrada.descripcion,
                solicitante=entrada.solicitante,
                contexto=entrada.contexto,
                texto=str(data.get("texto_base", texto_base)),
                tono_objetivo=str(data.get("tono_objetivo", "profesional")),
                palabras_clave_marca=list(data.get("palabras_clave_marca", [])),
            )
        )
        pasos.append(self._serializar_paso("voz_marca_inteligente", voz))
        trazas.extend([f"paso:voz_marca_inteligente:{traza}" for traza in voz.trazas])
        advertencias.extend(voz.advertencias)

        return pasos

    def _serializar_paso(self, nombre_paso: str, resultado: ResultadoSkill) -> dict[str, Any]:
        return {
            "paso": nombre_paso,
            "skill": resultado.nombre_skill,
            "estado": resultado.estado,
            "mensaje": resultado.salida.get("mensaje", ""),
            "trazas": resultado.trazas,
            "advertencias": resultado.advertencias,
            "salida": resultado.salida,
        }


def evaluar_orquestador_multiskill(entrada: SolicitudOrquestacion) -> ResultadoSkill:
    """API funcional para ejecutar pipelines multi-skill."""

    return OrquestadorMultiSkill().ejecutar(entrada)
