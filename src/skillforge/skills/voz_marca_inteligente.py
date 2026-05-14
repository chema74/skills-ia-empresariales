"""Skill 08: Voz de Marca Inteligente (V1 local)."""

from dataclasses import dataclass, field

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


TERMINOS_NO_RECOMENDADOS = [
    "siempre", "nunca", "garantizado", "100% seguro", "perfecto"
]


@dataclass
class SolicitudVozMarca(EntradaSkill):
    """Entrada para ajuste local de tono y estilo de marca."""

    texto: str = ""
    tono_objetivo: str = "profesional"
    palabras_clave_marca: list[str] = field(default_factory=list)


class VozMarcaInteligenteSkill(SkillBase):
    """Transforma texto a estilo profesional y verifica checklist."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="voz_marca_inteligente")

    def ejecutar(self, entrada: SolicitudVozMarca) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_voz_marca")

        if not entrada.texto.strip():
            self.nueva_traza(trazas, "texto_vacio")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Texto vacio: no hay contenido para adaptar"},
                trazas=trazas,
                advertencias=advertencias,
            )

        texto = " ".join(entrada.texto.strip().split())
        texto_adaptado = self._aplicar_tono(texto, entrada.tono_objetivo)

        checklist = {
            "tono_objetivo_aplicado": entrada.tono_objetivo in {"profesional", "cercano", "ejecutivo"},
            "sin_promesas_absolutas": True,
            "incluye_palabras_clave": True,
        }

        texto_min = texto_adaptado.lower()
        for term in TERMINOS_NO_RECOMENDADOS:
            if term in texto_min:
                checklist["sin_promesas_absolutas"] = False
                advertencias.append(f"termino no recomendado detectado: {term}")

        faltantes = [p for p in entrada.palabras_clave_marca if p.lower() not in texto_min]
        if faltantes:
            checklist["incluye_palabras_clave"] = False
            advertencias.append(f"faltan palabras clave de marca: {', '.join(faltantes)}")

        if entrada.tono_objetivo not in {"profesional", "cercano", "ejecutivo"}:
            advertencias.append("tono objetivo no estandar, se aplico ajuste profesional por defecto")

        self.nueva_traza(trazas, "texto_adaptado")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Voz de marca adaptada en local",
                "tono_objetivo": entrada.tono_objetivo,
                "texto_original": entrada.texto,
                "texto_adaptado": texto_adaptado,
                "checklist_marca": checklist,
            },
            trazas=trazas,
            advertencias=advertencias,
        )

    def _aplicar_tono(self, texto: str, tono: str) -> str:
        base = texto
        if tono == "ejecutivo":
            return f"Resumen ejecutivo: {base}"
        if tono == "cercano":
            return f"Te compartimos una actualización clara: {base}"
        return f"Comunicación profesional: {base}"


def evaluar_voz_marca_inteligente(entrada: SolicitudVozMarca) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return VozMarcaInteligenteSkill().ejecutar(entrada)