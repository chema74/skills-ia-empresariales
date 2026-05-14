"""Skill 07: Enrutador Inteligente (V1 local)."""

from dataclasses import dataclass, field

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


REGLAS_RUTA = {
    "documento": "lector_inteligente_documental",
    "anomalia": "radar_anomalias",
    "informe": "forjador_informes",
    "cliente": "memoria_contextual_cliente",
    "riesgo": "pulso_riesgo",
    "buscar": "buscador_privado_aumentado",
    "aprobacion": "puerta_aprobacion_humana",
}


@dataclass
class SolicitudEnrutamiento(EntradaSkill):
    """Entrada para decidir skill objetivo por intención."""

    intencion: str = ""
    metadatos: dict[str, str] = field(default_factory=dict)


class EnrutadorInteligenteSkill(SkillBase):
    """Selecciona skill objetivo y plan básico de ejecución."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="enrutador_inteligente")

    def ejecutar(self, entrada: SolicitudEnrutamiento) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_enrutamiento")

        texto = entrada.intencion.strip().lower()
        if not texto:
            self.nueva_traza(trazas, "intencion_vacia")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Intencion vacia: no se puede enrutar"},
                trazas=trazas,
                advertencias=advertencias,
            )

        coincidencias: list[str] = []
        for clave, skill in REGLAS_RUTA.items():
            if clave in texto:
                coincidencias.append(skill)

        self.nueva_traza(trazas, "coincidencias_detectadas")

        if not coincidencias:
            advertencias.append("sin coincidencias exactas: usar revisión humana para decidir ruta")
            destino = "revision_humana"
        elif len(set(coincidencias)) > 1:
            advertencias.append("intencion ambigua: múltiples skills candidatas")
            destino = coincidencias[0]
        else:
            destino = coincidencias[0]

        plan = [
            "validar_entrada",
            f"ejecutar_skill:{destino}",
            "validar_resultado",
            "registrar_trazas_locales",
        ]

        self.nueva_traza(trazas, "plan_generado")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Enrutamiento completado en local",
                "intencion": entrada.intencion,
                "skill_destino": destino,
                "skills_candidatas": sorted(set(coincidencias)),
                "plan_ejecucion": plan,
                "metadatos": entrada.metadatos,
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_enrutador_inteligente(entrada: SolicitudEnrutamiento) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return EnrutadorInteligenteSkill().ejecutar(entrada)