"""Utilidades de trazabilidad local para skills."""

from datetime import datetime, timezone


def crear_traza_local(evento: str) -> str:
    """Crea una traza local con sello temporal UTC."""

    marca = datetime.now(timezone.utc).isoformat()
    return f"local|{marca}|{evento}"


def agregar_traza_local(trazas: list[str], evento: str) -> list[str]:
    """Agrega una traza local y devuelve la lista actualizada."""

    trazas.append(crear_traza_local(evento))
    return trazas