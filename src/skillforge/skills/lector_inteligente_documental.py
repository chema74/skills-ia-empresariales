"""Skill 01: Lector Inteligente Documental (V1 local)."""

from dataclasses import dataclass, field

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


@dataclass
class SolicitudLecturaDocumental(EntradaSkill):
    """Entrada para lectura documental local."""

    texto_documento: str = ""
    max_secciones: int = 10
    palabras_clave: list[str] = field(default_factory=list)


class LectorInteligenteDocumentalSkill(SkillBase):
    """Extrae secciones y señales básicas de un documento local."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="lector_inteligente_documental")

    def ejecutar(self, entrada: SolicitudLecturaDocumental) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_lectura_documental")

        if not entrada.texto_documento.strip():
            self.nueva_traza(trazas, "documento_vacio")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Documento vacio: no hay contenido para analizar"},
                trazas=trazas,
                advertencias=advertencias,
            )

        bloques = [b.strip() for b in entrada.texto_documento.split("\n\n") if b.strip()]
        secciones = bloques[: max(1, entrada.max_secciones)]
        self.nueva_traza(trazas, "secciones_extraidas")

        resumen = []
        for i, sec in enumerate(secciones, start=1):
            primera_linea = sec.splitlines()[0][:120]
            resumen.append(f"S{i}: {primera_linea}")

        palabras_detectadas: dict[str, int] = {}
        texto_min = entrada.texto_documento.lower()
        for palabra in entrada.palabras_clave:
            p = palabra.strip().lower()
            if not p:
                continue
            conteo = texto_min.count(p)
            if conteo > 0:
                palabras_detectadas[p] = conteo

        if not palabras_detectadas and entrada.palabras_clave:
            advertencias.append("no se detectaron palabras clave solicitadas")

        self.nueva_traza(trazas, "resumen_generado")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Lectura documental completada en local",
                "total_secciones": len(secciones),
                "resumen_secciones": resumen,
                "palabras_detectadas": palabras_detectadas,
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_lector_inteligente_documental(entrada: SolicitudLecturaDocumental) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return LectorInteligenteDocumentalSkill().ejecutar(entrada)