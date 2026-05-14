"""Contratos comunes para las skills del repositorio."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EntradaSkill:
    """Entrada comun para ejecuciones de skills."""

    accion: str
    descripcion: str
    solicitante: str
    contexto: dict[str, Any] = field(default_factory=dict)


@dataclass
class ResultadoSkill:
    """Resultado estandar de ejecucion de una skill."""

    nombre_skill: str
    estado: str
    salida: dict[str, Any]
    trazas: list[str]
    advertencias: list[str]

    def es_correcto(self) -> bool:
        """Devuelve True cuando el estado de ejecucion es correcto."""

        return self.estado == "ok"