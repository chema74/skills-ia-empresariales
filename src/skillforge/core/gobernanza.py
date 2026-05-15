"""Utilidades de gobernanza para aprobaciones humanas y auditoria."""

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
POLITICAS_PATH = ROOT / "configs" / "gobernanza" / "politicas_aprobacion_v1.json"
REGISTRO_CAMBIOS_PATH = ROOT / "configs" / "gobernanza" / "registro_cambios_gobernanza.json"


@dataclass(frozen=True)
class PoliticaAprobacion:
    """Politica de aprobacion para una accion sensible."""

    accion: str
    nivel_riesgo: str
    requiere_aprobacion: bool
    roles_aprobadores: list[str]
    requiere_evidencia: bool
    version: str


@lru_cache(maxsize=1)
def cargar_politicas() -> dict[str, PoliticaAprobacion]:
    data = _leer_json(POLITICAS_PATH)
    version = str(data.get("version", "desconocida"))
    politicas_raw = data.get("politicas", [])
    politicas: dict[str, PoliticaAprobacion] = {}

    for item in politicas_raw:
        if not isinstance(item, dict):
            continue
        accion = str(item.get("accion", "")).strip().lower()
        if not accion:
            continue
        politica = PoliticaAprobacion(
            accion=accion,
            nivel_riesgo=str(item.get("nivel_riesgo", "medio")),
            requiere_aprobacion=bool(item.get("requiere_aprobacion", True)),
            roles_aprobadores=[str(rol).strip().lower() for rol in item.get("roles_aprobadores", [])],
            requiere_evidencia=bool(item.get("requiere_evidencia", True)),
            version=version,
        )
        politicas[accion] = politica

    return politicas


@lru_cache(maxsize=1)
def cargar_registro_cambios() -> list[dict[str, Any]]:
    data = _leer_json(REGISTRO_CAMBIOS_PATH)
    cambios = data.get("cambios", [])
    return cambios if isinstance(cambios, list) else []


def _leer_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    contenido = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(contenido, dict):
        return contenido
    return {}
