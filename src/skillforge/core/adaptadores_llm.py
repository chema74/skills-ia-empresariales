"""Capa de adaptadores LLM opcionales con fallback local garantizado."""

import os
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class RespuestaAdaptadorLLM:
    """Contrato comun de respuesta para adaptadores LLM."""

    proveedor: str
    estado: str
    texto: str
    tokens_estimados: int
    error: str | None = None


class AdaptadorLLM(Protocol):
    """Protocolo comun para adaptadores de proveedores LLM."""

    nombre: str

    def disponible(self) -> bool:
        """Indica si el proveedor esta disponible en el entorno."""

    def generar(self, prompt: str, temperatura: float = 0.2, max_tokens: int = 240) -> RespuestaAdaptadorLLM:
        """Genera texto para un prompt usando el proveedor."""


class AdaptadorLocalReglas:
    """Fallback local sin dependencias externas."""

    nombre = "local_reglas"

    def disponible(self) -> bool:
        return True

    def generar(self, prompt: str, temperatura: float = 0.2, max_tokens: int = 240) -> RespuestaAdaptadorLLM:
        prompt_limpio = " ".join(prompt.split())
        if not prompt_limpio:
            texto = "No se recibio contenido para generar salida."
        else:
            texto = f"Salida local-first: {prompt_limpio[:max_tokens]}"
        return RespuestaAdaptadorLLM(
            proveedor=self.nombre,
            estado="ok",
            texto=texto,
            tokens_estimados=min(max_tokens, max(1, len(texto) // 4)),
            error=None,
        )


class AdaptadorMockGroq:
    """Proveedor opcional simulado para validacion de integracion V8."""

    nombre = "mock_groq"

    def disponible(self) -> bool:
        return os.getenv("SKILLFORGE_ENABLE_MOCK_GROQ", "0") == "1"

    def generar(self, prompt: str, temperatura: float = 0.2, max_tokens: int = 240) -> RespuestaAdaptadorLLM:
        if not self.disponible():
            return RespuestaAdaptadorLLM(
                proveedor=self.nombre,
                estado="error",
                texto="",
                tokens_estimados=0,
                error="Proveedor mock_groq no habilitado en entorno",
            )
        prompt_limpio = " ".join(prompt.split())
        texto = f"MockGroq respuesta: {prompt_limpio[:max_tokens]}"
        return RespuestaAdaptadorLLM(
            proveedor=self.nombre,
            estado="ok",
            texto=texto,
            tokens_estimados=min(max_tokens, max(1, len(texto) // 4)),
            error=None,
        )


ADAPTADORES_REGISTRADOS: dict[str, AdaptadorLLM] = {
    "mock_groq": AdaptadorMockGroq(),
    "local_reglas": AdaptadorLocalReglas(),
}


def listar_adaptadores() -> list[str]:
    """Lista los adaptadores registrados."""

    return sorted(ADAPTADORES_REGISTRADOS.keys())


def generar_con_fallback(
    prompt: str,
    proveedor_preferido: str = "mock_groq",
    temperatura: float = 0.2,
    max_tokens: int = 240,
) -> tuple[RespuestaAdaptadorLLM, bool]:
    """Genera salida con proveedor opcional y fallback local garantizado.

    Devuelve una tupla con la respuesta final y un indicador de si hubo fallback.
    """

    adaptador_preferido = ADAPTADORES_REGISTRADOS.get(proveedor_preferido)
    if adaptador_preferido is not None:
        respuesta = adaptador_preferido.generar(prompt=prompt, temperatura=temperatura, max_tokens=max_tokens)
        if respuesta.estado == "ok":
            return respuesta, False

    fallback = ADAPTADORES_REGISTRADOS["local_reglas"].generar(
        prompt=prompt,
        temperatura=temperatura,
        max_tokens=max_tokens,
    )
    return fallback, True
