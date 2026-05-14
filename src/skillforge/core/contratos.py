"""Contratos comunes para las skills del repositorio."""

from dataclasses import dataclass
from typing import Any


@dataclass
class ResultadoSkill:
    """Resultado estándar de ejecución de una skill."""

    nombre_skill: str
    estado: str
    salida: dict[str, Any]
    trazas: list[str]
    advertencias: list[str]

    def es_correcto(self) -> bool:
        """Devuelve True cuando el estado de ejecución es correcto."""

        return self.estado == "ok"
