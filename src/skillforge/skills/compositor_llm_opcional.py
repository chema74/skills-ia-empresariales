"""Skill V8: Compositor con proveedor LLM opcional y fallback local."""

from dataclasses import dataclass

from skillforge.core.adaptadores_llm import generar_con_fallback, listar_adaptadores
from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


@dataclass
class SolicitudComposicionLLM(EntradaSkill):
    """Entrada para composicion de texto con proveedor opcional."""

    prompt: str = ""
    proveedor_preferido: str = "mock_groq"
    temperatura: float = 0.2
    max_tokens: int = 240


class CompositorLLMOpcionalSkill(SkillBase):
    """Genera texto con adaptador opcional y fallback local."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="compositor_llm_opcional")

    def ejecutar(self, entrada: SolicitudComposicionLLM) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_composicion_llm_opcional")

        if not entrada.prompt.strip():
            self.nueva_traza(trazas, "prompt_vacio")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Prompt vacio: define contenido para composicion"},
                trazas=trazas,
                advertencias=advertencias,
            )

        self.nueva_traza(trazas, f"intento_proveedor:{entrada.proveedor_preferido}")
        respuesta, uso_fallback = generar_con_fallback(
            prompt=entrada.prompt,
            proveedor_preferido=entrada.proveedor_preferido,
            temperatura=entrada.temperatura,
            max_tokens=entrada.max_tokens,
        )

        if uso_fallback:
            advertencias.append(
                f"fallback activado: proveedor '{entrada.proveedor_preferido}' no disponible o con error"
            )
            self.nueva_traza(trazas, "fallback_local_activado")
        else:
            self.nueva_traza(trazas, f"proveedor_activo:{respuesta.proveedor}")

        self.nueva_traza(trazas, "fin_composicion_llm_opcional")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Composicion completada con capa LLM opcional",
                "proveedor_solicitado": entrada.proveedor_preferido,
                "proveedor_efectivo": respuesta.proveedor,
                "uso_fallback_local": uso_fallback,
                "texto_generado": respuesta.texto,
                "tokens_estimados": respuesta.tokens_estimados,
                "adaptadores_disponibles": listar_adaptadores(),
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_compositor_llm_opcional(entrada: SolicitudComposicionLLM) -> ResultadoSkill:
    """API funcional para composicion con adaptadores opcionales."""

    return CompositorLLMOpcionalSkill().ejecutar(entrada)
