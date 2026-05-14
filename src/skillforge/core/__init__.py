"""Nucleo comun compartido entre skills."""

from .contratos import ResultadoSkill
from .trazabilidad import agregar_traza_local, crear_traza_local
from .validacion import validar_resultado_skill

__all__ = [
    "ResultadoSkill",
    "agregar_traza_local",
    "crear_traza_local",
    "validar_resultado_skill",
]