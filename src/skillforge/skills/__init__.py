"""Modulo contenedor de skills empresariales."""

from .puerta_aprobacion_humana import (
    ACCIONES_SENSIBLES,
    SolicitudAprobacion,
    evaluar_puerta_aprobacion_humana,
)

__all__ = [
    "ACCIONES_SENSIBLES",
    "SolicitudAprobacion",
    "evaluar_puerta_aprobacion_humana",
]